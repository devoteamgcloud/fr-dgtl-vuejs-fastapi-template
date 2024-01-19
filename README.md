# cookiecutter-vuejs-fastapi-template

& FastApi Stack

This repository provides:

- a [VueJS](https://vuejs.org) base stack:

  - Customizable layout (Navbar, Sidebar, Footer) & generic components with [Vuetify](https://vuetify.com)
  - API axios client wrapped into reusable service
  - Form validation & unit tests
  - Dark theme & i18n support

- a [FastAPI](https://fastapi.tiangolo.com/) base stack integrated with [GCP](https://console.cloud.google.com/)
  - Runnable from VSCode launch with or without docker containers
  - Generic [Firestore](https://firebase.google.com/docs/firestore?hl=fr) client (authentication with [ADC](https://cloud.google.com/docs/authentication/provide-credentials-adc?hl=fr))
  - Environment injection from .env file

These templates are:

- Based on [cookiecutter](https://www.cookiecutter.io/)
- Auto-pushable on Github when generated
- Auto-deployable on [Cloud Run](https://cloud.google.com/run).

## Installation

Install dependencies

```bash
cd cookiecutter-vuejs-fastapi-template
python3 -m pip install -r requirements.txt
# Open provided workspace
code .vscode/cookiecutter.code-workspace
```

## Generate Frontend Project

Use this repository to generate a Vuejs template project

```bash
cookiecutter cookiecutter-vuejs-fastapi-template/frontend   # Will ask your needs from cookiecutter.json
```

- **'repository_name'** allows you to specify an empty-existing Git repository to push the template on.

```bash
<github_username>/<repo_name>  # Required format
```

If specified, it will auto-commit the generated template both in develop, uat & main branches.
Ensure you have corrects **SSH rights & access**

- **'project_name'** is the name on the top of ReadMe.

- **'project_slug'** is the name of the generated folder

- **'description'** will be added under the project name in the ReadMe.

- **'maintainer'** has an informativ goal (not used in the template)

- **'navbar'** integrate a navbar with i18n support, and a dark mode switch.

- **'sidebar'** integrate a left sidebar with navigation.

- **'footer'** integrate a footer.

- **'as_container'** allow you to dockerize local run and auto deploy on Cloud Run

## Generate Backend Project

Use this repository to generate a FastApi template project

```bash
cookiecutter cookiecutter-vuejs-fastapi-template/backend   # Will ask your needs from cookiecutter.json
```

- **'repository_name'** allows you to specify an empty-existing Git repository to push the template on.

```bash
<github_username>/<repo_name>  # Required format
```

- **'project_name'** is the name on the top of ReadMe.

- **'project_slug'** is the name of the generated folder

- **'description'** will be added under the project name in the ReadMe.

- **'maintainer'** has an informativ goal (not used in the template)

- **'as_container'** allow you to dockerize local run and auto deploy on Cloud Run

- **'gcloud_project'** is the GCP project ID on which the project will be deployed

## Automate Cloud Run deployment

Create a Cloud Build trigger for each repository on you Google Cloud Project and specify the cloudbuild.yaml path

Deployment will then run automatically based on your conditions

### TODO

#### Back

- Allow to choose either Firestore or SQL + use multi cookiecutter.json

#### Both

- Add access token to .env & check existence after project creation to call Github API & manage branches protections
