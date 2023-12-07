# cookie-cutter-vuejs-fastapi-template

VueJs & FastApi Stack template based on [cookiecutter](https://www.cookiecutter.io/)

## Installation

Install dependencies

```bash
cd cookiecutter-vuejs-fastapi-template
python3 -m pip install -r requirements.txt
```

## Usage

### Workspace

To open the template in VSCode, use the following command

```bash
cd cookiecutter-vuejs-fastapi-template
code .vscode/cookiecutter.code-workspace
```

### Generate Frontend Project

Use this repository to generate a Vuejs template project

```bash
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

- **'as_container'** allow you to dockerize local run and auto deploy on Cloud Run

### Generate Backend Project (WIP)

Use this repository to generate a FastApi template project

```bash
cookiecutter cookiecutter-vuejs-fastapi-template/backend   # Will ask your needs from cookiecutter.json
```

- **'project_name'** is the name on the top of ReadMe.

- **'project_slug'** is the name of the generated folder

- **'description'** will be added under the project name in the ReadMe.

- **'maintainer'** has an informativ goal (not used in the template)

### TODO

#### Front

- Add another tab/page for routing example
- Generic components : Tables

#### Back

- Allow to choose either Firestore or SQL + use multi cookiecutter.json

#### Both

- CookieCut Dockerfile questions (For both Front & Back, & docker-compose)
