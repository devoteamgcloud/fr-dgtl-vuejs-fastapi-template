# {{cookiecutter.project_name}}

{{ '=' * cookiecutter.project_name|length }}

## Description

{{cookiecutter.description}}

## Template Stack

- [FastApi](https://fastapi.tiangolo.com/)

## Project Setup

- Install [Poetry](https://python-poetry.org/docs/)

- Set config for venv in local

```bash
poetry config virtualenvs.in-project true
poetry install

```

### Compile and Hot-Reload for Development

```sh
poetry shell                  # Launch terminal with dependencies
uvicorn app.main:app --reload # Or from VSCode launcher
```

## Api docs

- [Swagger](http://localhost:8000/docs)

### Maintainers

{{cookiecutter.maintainer}}
