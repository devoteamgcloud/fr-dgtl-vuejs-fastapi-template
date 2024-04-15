# Cookiecutter Template Generation

This repository provides:

- a [VueJS](https://vuejs.org) base stack:

  - Customizable layout (Navbar, Sidebar, Footer) & generic components with [Vuetify](https://vuetify.com)
  - API axios client wrapped into reusable service
  - Form validation & unit tests
  - Dark theme & i18n support

- a [FastAPI](https://fastapi.tiangolo.com/) base stack:
  - Runnable from VSCode launch with or without docker containers
  - Generic [Firestore](https://firebase.google.com/docs/firestore?hl=fr) client (authentication with [ADC](https://cloud.google.com/docs/authentication/provide-credentials-adc?hl=fr))
  - Generic [PostgreSQL](https://www.postgresql.org/about/) async client wrapped with [SQLModel](https://sqlmodel.tiangolo.com/) (SQLAlchemy 2.0)

These templates are:

- Based on [cookiecutter](https://www.cookiecutter.io/)
- Auto-pushable on Github when generated
- Auto-deployable on [Cloud Run](https://cloud.google.com/run).

It assumes that each template is pushed on a separate Github repository

## Installation

- Install dependencies

  ```bash
  cd cookiecutter-vuejs-fastapi-template
  python3 -m pip install -r requirements.txt

  # Open provided workspace
  code .vscode/cookiecutter.code-workspace
  ```

- Copy .env in both folders

  Do not modify 'cookiecutter.key' values (replaced at generation)

  ```bash
  # In frontend/
    VITE_BASE_URL="http://localhost:8000/api"
    # (Optional): Used to set branch protection
    GITHUB_ACCESS_TOKEN="<PERSONAL_ACCESS_TOKEN>"

    # For deployed version
    VITE_BASE_URL="https://<BACK_SERVICE_NAME>-<PROJECT_NUMBER>.{{ cookiecutter.gcloud_region }}.run.app/api"
  ```

  ```bash
  # In backend/
    ENV="local"
    GCLOUD_PROJECT_ID="{{cookiecutter.gcloud_project}}"
    # (Optional): Used to set branch protection
    GITHUB_ACCESS_TOKEN="<PERSONAL_ACCESS_TOKEN>"
    SQLALCHEMY_DATABASE_URI="postgresql+asyncpg://postgres:postgres@localhost:5434/{{cookiecutter.project_slug}}_db"

    # For deployed version
    ENV="dev"
    SQLALCHEMY_DATABASE_URI='postgresql+asyncpg://postgres:postgres@/{{cookiecutter.project_slug}}_db?host=/cloudsql/{{cookiecutter.gcloud_project}}:{{ cookiecutter.gcloud_region }}:{{ cookiecutter.project_slug.replace('_', '-') }}-instance'
    BACKEND_CORS_ORIGINS=["https://<FRONT_SERVICE_NAME>-<PROJECT_NUMBER>.{{ cookiecutter.gcloud_region }}.run.app"]

## Generate Frontend Project

Use this repository to generate a Vuejs template project

```bash
cookiecutter cookiecutter-vuejs-fastapi-template/frontend   # Will ask your needs from cookiecutter.json
```

- **'repository_name'** allows you to specify an empty-existing Git repository to push the template on.

  ```bash
  <github_username>/<repo_name>  # Required format

  # 1. Ensure you have corrects SSH rights & access

  # 2. This will also set branch protection if you specified GITHUB_ACCESS_TOKEN variable in .env.
  # Change settings as your convenience in hooks_modules/branch_protection.json
  ```

- **'project_name'** is the name on the top of ReadMe.

- **'project_slug'** is the name of the generated folder

- **'description'** will be added under the project name in the ReadMe.

- **'maintainer'** has an informativ goal (not used in the template)

- **'navbar'** integrate a navbar with i18n support, and a dark mode switch.

- **'sidebar'** integrate a left sidebar with navigation.

- **'footer'** integrate a footer.

- **'as_container'** provide local dockerization and auto deploy on Cloud Run

## Generate Backend Project

Use this repository to generate a FastApi template project

```bash
cookiecutter cookiecutter-vuejs-fastapi-template/backend   # Will ask your needs from cookiecutter.json
```

- **'repository_name'** allows you to specify an empty-existing Git repository to push the template on.

  ```bash
  <github_username>/<repo_name>  # Required format

  # 1. Ensure you have corrects SSH rights & access

  # 2. This will also set branch protection if you specified GITHUB_ACCESS_TOKEN variable in .env.
  # Change settings as your convenience in hooks_modules/branch_protection.json
  ```

- **'project_name'** is the name on the top of ReadMe.

- **'project_slug'** is the name of the generated folder

- **'description'** will be added under the project name in the ReadMe.

- **'maintainer'** has an informativ goal (not used in the template)

- **'database'** make you choose which type of database will be provided (Firestore, PostgreSQL with SQLModel, or Both)

- **'as_container'** provide local dockerization and auto deploy on Cloud Run

- **'gcloud_project'** is the GCP project ID on which the project will be deployed

## CICD

Each template has its own github actions for generating the template, install dependencies, runs dev server & unit tests.

You can try github actions locally from root folder using [act](https://nektosact.com/):

```bash
act -j test-run-template --rm -W .github/workflows/frontend_template.yaml
act -j test-run-template --rm -W .github/workflows/backend_template.yaml
```

## TODO

Deployment:

- Add a specific database user and not postgres

Backend:

- Optimize unit tests (bad scope fixture)

Frontend:

- Add User entity into TableView
- Add edit action into TableView
