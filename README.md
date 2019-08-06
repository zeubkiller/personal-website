# Personal website

Personal website served with a flask server

## How to install the dev environment

This project work with Flask and Python 3.7.

1. You can install and download conda or miniconda.
2. Create a new environment with Python 3.7 then install pip
3. Use the requirements.txt to install all the python dependencies

## How to run

1. Assign the entry point of your server to the FLASK_APP variable
On linux:

```sh
export FLASK_APP=***.py
```

2. Then to launch the server

```sh
flask run
```

## Folder structure

* Everything about the server code should be in the app/ folder.
* Each folder should contain a __init__.py file.

## Specific command

### Project command

* To set up the debug mode

```sh
export FLASK_ENV=development
```

### Basic command

#### Conda

List all environments

```sh
conda info -e
```

Activate an environment

```sh
conda activate ***
```
