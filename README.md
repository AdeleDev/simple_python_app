# Simple Python App example

Very easy python project example - fitness tracker module.
Module performs the following functions:
* receive information about the past training from the sensor unit,
* determine the type of training
* calculate the results of training,
* display an informational message about the results of the training.

The information message includes:
* type of training (running, walking or swimming);
* duration of the workout;
* distance covered by the user, in kilometers;
* average speed at a distance, in km/h;
* energy expenditure, in kilocalories.

### Built With

* [![Python][Python.io]][Python-url]


## Pre-installations

#### Clone the repo:

```sh
git clone https://github.com/AdeleDev/simple_python_app.git
```

#### Start and activate virtual environment:

```sh
python3 -m venv env
```

```sh
source env/bin/activate
```

#### Setup dependencies from requirements.txt file:
```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

## Usage

#### Test data:
Tuple with 2 elements:
* code designation of the last workout (Swimming, Running or Walking)
* list of indicators received from the device's sensors

Data example: 

```
packages = [
     ('SWM', [720, 1, 80, 25, 40]),
     ('RUN', [15000, 1, 75]),
     ('WLK', [9000, 1, 75, 180]),
 ] 
```

#### Run project:

```sh
python .\fitnessTracker.py 
```

<!-- MARKDOWN LINKS & IMAGES -->

[Python.io]: https://img.shields.io/badge/-Python-yellow?style=for-the-badge&logo=python

[Python-url]: https://www.python.org/
