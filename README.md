# Description

This is a sample web API written on Python3 with flask framework.
There is no adequate usage for this API, because it was made only for my education.
Still, there is a small chance that it will evolve in something useful.

## Requirements

- Python3

#### python3 installed modules

- pip
- venv (or virualenv)

## Installation

> *NOTE: use "venv" as the name of virtual environment directory (as below) — it's already declared in .gitignore so you won't have to edit this file*

        $ git clone <repo link>
        $ cd sample-http-api
        $ python3 -m venv venv    # venv module usage, use virtualenv here if you want
        $ . venv/bin/activate
        (venv)$ python3 -m pip install -r requirements.txt

## Usage

### Debug

You can call it "single user mode" - it is able to process one request at a time.

Just invoke script by Python 3

    (venv)$ python3 api.py

### Production (if you accidentally need it)

Use any WSGI server to handle more than one request at once (unlike flask 
built-in `run()` method). One of WSGI servers is [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)

Install uWSGI as module inside environment

    (venv)$ python3 -m pip install uwsgi

and run uWSGI with command

    $ uwsgi --socket 0.0.0.0:3031 --wsgi-file api.py --callable app --processes 4 --threads 2 --stats 0.0.0.0:9191

## Author

Nick Belousov a.k.a. Trofogol
