# Description

This is a sample web API written on Python3 with flask framework.
There is no adequate usage for this API, because it was made only for my education.
Still, there is a small chance that it will evolve in something useful.

> This [Vagrant project](https://github.com/Trofogol/vagrant-api-environment) builds and launch it automatically.

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

    $ uwsgi --wsgi-file api.py --callable app --processes 4 --threads 2 --http 0.0.0.0:9191

> Useful flags for `uwsgi`: `--socket <address>:<port>` (for proxy, e.g. nginx); `--stats <address>:<port>` (get server stats)

### Debian package

**Unpacking does not work properly, this section is TODO note**

This project has been debianized to be packed in Debian package. However, 
I still don't understand how to organize project layout to get access to unpacked version.

***TODO:***
- fully understand python packaging by [setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
 (also read [legacy docs](https://docs.python.org/3/distutils/): setuptools' docs could lack some info)
- rework project layout and scripts to make them work and accessible after unpacking
