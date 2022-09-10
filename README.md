# Service My Car Please

Project to check when to service auto consumables.

[![Django version](https://img.shields.io/badge/Django-3.2.15-informational)](https://www.djangoproject.com/)
[![Python version](https://img.shields.io/badge/Python-3.10-informational)](https://www.python.org/)
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![CI passing](https://github.com/vanya909/smcp/actions/workflows/ci.yml/badge.svg)](https://github.com/vanya909/smcp/actions)
[![License](https://shields.io/github/license/vanya909/smcp)](https://github.com/vanya909/smcp/blob/main/LICENSE)
![Commit activity](https://img.shields.io/github/commit-activity/m/vanya909/smcp?color=purple)

## Installation

Build the stack:
```bash
$ docker-compose -f local.yml build
```

Initialize git hooks
```bash
$ pre-commit install
```

To up the stack just use:
```bash
$ docker-compose -f local.yml up
```

## Management Commands
To run management commands use:
```bash
$ docker-compose -f local.yml run --rm django python manage.py <command>
```
