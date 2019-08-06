# Personal website

Personal website served with a flask server

## How to run

* Assign the entry point of your server to the FLASK_APP variable
On linux:

```sh
export FLASK_APP=***.py
```

* Then to launch the server

```sh
flask run
```

## Folder structure

* Everything about the server code should be in the app/ folder.
* Each folder should contain a __init__.py file.

## Specific command

* To set up the debug mode

```sh
export FLASK_ENV=development
```
