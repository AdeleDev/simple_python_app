from dataclasses import dataclass
from typing import ClassVar, List, Dict, Type


@dataclass
class InfoMessage:
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    training_type: str

    def get_message(self) -> str:
        return (f'Training type: {self.training_type}; '
                f'Length: {self.duration:.3f} ч.; '
                f'Distance: {self.distance:.3f} km; '
                f'Avg. speed: {self.speed:.3f} km/h; '
                f'Lost calories: {self.calories:.3f}.')


class Training:
    """Basic training class."""
    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[int] = 1000
    MINUTES: ClassVar[int] = 60

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        raise NotImplementedError(f'Not implemented in {type(self).__name__}')

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(
            self.__class__.__name__, self.duration,
            self.get_distance(), self.get_mean_speed(),
            self.get_spent_calories())


class Running(Training):
    COEFF_CALORIE_1: ClassVar[int] = 18
    COEFF_CALORIE_2: ClassVar[int] = 20

    def get_spent_calories(self) -> float:
        return ((self.COEFF_CALORIE_1 * self.get_mean_speed()
                 - self.COEFF_CALORIE_2) * self.weight / self.M_IN_KM
                * self.duration * self.MINUTES)


class SportsWalking(Training):
    COEFF_CALORIE_1: ClassVar[float] = 0.035
    COEFF_CALORIE_2: ClassVar[float] = 0.029

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    @property
    def duration_in_min(self):
        return self.duration * self.MINUTES

    def get_spent_calories(self) -> float:
        return ((self.COEFF_CALORIE_1 * self.weight + (self.get_mean_speed()
                                                       ** 2 // self.height)
                 * self.COEFF_CALORIE_2 * self.weight) * self.duration_in_min)


class Swimming(Training):
    LEN_STEP: ClassVar[float] = 1.38
    COEFF_CALORIE: ClassVar[float] = 1.1

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            length_pool: float,
            count_pool: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + self.COEFF_CALORIE) * 2 * self.weight

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration
                )


def read_package(workout_type: str, data: List[int]) -> Training:
    selector: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in selector:
        raise KeyError(
            f'Unsupported workout_type. Please send one of '
            f'{selector.keys()}')
    return selector[workout_type](*data)


def main(training: Training) -> None:
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
