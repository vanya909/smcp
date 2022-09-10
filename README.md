# Service My Car Please

Project to check when to service auto consumables.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![CI passing](https://github.com/vanya909/smcp/actions/workflows/ci.yml/badge.svg)](https://github.com/vanya909/smcp/actions)

License: MIT

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
