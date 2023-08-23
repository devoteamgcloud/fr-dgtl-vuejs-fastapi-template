# cookie-cutter-vuejs-fastapi-template

VueJs & FastApi Stack template based on [cookiecutter](https://www.cookiecutter.io/)

## Installation

Install dependencies

```bash
cd cookiecutter-vuejs-fastapi-template
python3 -m pip install -r requirements.txt
```

## Usage

### Frontend

Use this repository to generate a Vuejs template project

```bash
cd ..
cookiecutter cookiecutter-vuejs-fastapi-template/frontend   # Will ask your needs from cookiecutter.json
```

- **'repository_name'** allows you to specify an empty-existing Git repository.

```bash
<github_username>/<repo_name>  # Required format
```

If specified, it will auto-commit the generated template both in develop, uat & main branches.
Ensure you have corrects  **SSH rights & access**

- **'project_name'** is the name on the top of ReadMe.

- **'project_slug'** is the name of the generated folder

- **'description'** will be added under the project name in the ReadMe.

- **'maintainer'** has an informativ goal (not used in the template)

- **'navbar'** allow you to choose if you want an existing navbar on first run.

- **'sidebar'** allow you to choose if you want an existing left sidebar on first run.

- **'footer'** allow you to choose if you want an existing footer on first run.

### Backend (WIP)

Use this repository to generate a FastApi template project

```bash
cookiecutter cookiecutter-vuejs-fastapi-template/backend   # Will ask your needs from cookiecutter.json
```

### TODO

- CookieCut a FastApi project (Allow to choose either Firestore or SQL + use multi cookiecutter.json)
- CookieCut a deployment method (App Engine, Cloud Run...)
