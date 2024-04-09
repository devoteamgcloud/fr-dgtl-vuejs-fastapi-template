# {{cookiecutter.project_name}}

{{ '=' * cookiecutter.project_name|length }}

## Description

{{cookiecutter.description}}

## Template Stack

- [FastApi](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [SQLAlchemy 2](https://docs.sqlalchemy.org/en/20/)

## Project Setup

- Install [Poetry](https://python-poetry.org/docs/)

- Set config for venv in local

  ```sh
  poetry config virtualenvs.in-project true
  poetry env use 3.11
  poetry install
  ```

- Create and run required databases

  ```bash
  docker compose up -d
  ```

- Apply migrations

  ```sh
  alembic upgrade head
  ```

### Run locally

```sh
# WITHOUT DOCKER (Guess ADC from env)
uvicorn app.main:app --reload          # Or from VSCode launcher

# OR

# WITH DOCKER
Use the launch.json configuration to build and run the container

# (Running the launch is an equivalent to):
docker build -t <image>:<tag> -f Dockerfile .
docker run --name {{ cookiecutter.project_slug }} -p 8000:8000 -p 5678:5678 -v "$HOME/.config/gcloud/application_default_credentials.json":/gcp/creds.json --env GOOGLE_APPLICATION_CREDENTIALS=/gcp/creds.json --env GCLOUD_PROJECT={{ cookiecutter.gcloud_project }} <image>:<tag>

```

## Tests

```sh
poetry run pytest --cov=app --cov-report=term     # Uses SQLALCHEMY_DATABASE_URI in pyproject.toml
```

## CI/CD

### CI with Github Actions

Use .github/workflows/lint.yaml **by enabling Github Actions API** in your repository

This will run linting for every Pull Request on develop, uat and master branches

### CD with Cloud Build & Cloud Run

.cloudbuild/cloudbuild.yaml is used automatically to deploy to Cloud Run according to your Cloud Build trigger configuration

*Requirements*:

- Create a Cloud Build trigger from GCP:
  - Specify the cloudbuild.yaml path
  - Give repository access to Cloud Build

- Add .env in a Secret named '{{ cookiecutter.project_slug.replace('_', '-') }}'

- APIs enabled:

  - Cloud Build API
  - Cloud Run API
  - Secret Manager API
  - Cloud SQL API

- Roles:

  - Cloud Build Service Account has Cloud Run Admin role
  - Cloud Build Service Account has Secret Manager Secret Accessor role

### Cloud Run & Cloud SQL

- Add a Cloud SQL instance named '{{ cookiecutter.project_slug.replace('_', '-') }}-instance'

- Add a database into the instance named '{{cookiecutter.project_slug}}_db'

- Run migrations into the instance with Cloud SQL Proxy

Note: The connection name of the SQL instance is automatically added to Cloud Run configuration while it's deploy

## Api docs

- [Swagger](http://localhost:8000/api/docs)

### Maintainers

{{cookiecutter.maintainer}}
