[![Build Status](https://travis-ci.org/RonaldoMPF/ToPresente.svg?branch=master)](https://travis-ci.org/RonaldoMPF/ToPresente)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)
<br />

# ToPresente
PROFESSOR, TÔ PRESENTE! - Projeto da disciplina de Inteligência Artificial 2018.1

PROFESSOR, TÔ PRESENTE! - Course Project (Artificial Intelligence 2018.1)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

python 2.7 or python 3.5

pip2 or pip3

tox

dlib already installed with Python bindings

**Optionally**: venv

### Installing

The installation will be exemplified using python 3.x  and pip3 but the same could be 
accomplished using python 2.7 and pip2

Clone and enter the directory using cd

```
git clone https://github.com/RonaldoMPF/ToPresente.git

cd ToPresente
```

Use venv to keep dependencies tidy, but you may opt not to use it.
Create a new directory inside the project directory where will keep the dependencies as 'venv'.

```
python3 -m venv ./venv
```

Source the venv to activate it.

```
source venv/bin/activate
```

Use pip to install the requirements

```
pip3 install -r requirements.txt
```

Run setup to generate project binary

```
python3 setup.py install
```

Binary will be available to be run inside venv directory

```
./venv/bin/to_presente
```

## Running the tests

Assuming tox is installed and we're inside the project

Run all enviroments (both python 2.7 and python 3.5)

```
tox
```

You can run the tests for python 2.7 

```
tox -e py27
```

You can run the tests for python 3.5

```
tox -e py35
```

## Authors

* **Benardi Nunes** - *Setup, Test integration and bash experiment* - [Benardi](https://github.com/Benardi)

See also the list of [contributors](https://github.com/RonaldoMPF/ToPresente/contributors) who participated in this project.

## Built With

* [Dlib](http://dlib.net/) - Modern C++ toolkit containing machine learning algorithms 
* [Face Recognition](http://face-recognition.readthedocs.io/en/latest/) -  Python face recognition library
* [Tox](https://tox.readthedocs.io/en/latest/) - Automate and standardize testing in Python


