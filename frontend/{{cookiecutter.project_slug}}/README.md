# {{cookiecutter.project_name}}

{{ '=' * cookiecutter.project_name|length }}

## Description

{{cookiecutter.description}}

## Template Stack

- [Vue3 with Composition API](https://vuejs.org/guide/introduction.html)
- [Vuetify](https://vuetifyjs.com/en/getting-started/installation/)
- [Pinia](https://pinia.vuejs.org/)
- [piniaPluginPersistedstate](https://github.com/prazdevs/pinia-plugin-persistedstate/)

## Formatting / Linting

The template is using [ESLint for VueJS](https://eslint.vuejs.org/).

By default, **auto formatting is enabled on save**.

## I18N

To add any new langage:

- Add new languages in JSON format to `i18n` directory
- Complete 'languages' & 'countries_info' variables in `i18n/index.js`

(see [vue-i18n](https://kazupon.github.io/vue-i18n/) for more documentation)

(see [vue-country-flag-next](https://www.npmjs.com/package/vue-country-flag-next) for country flags)

## Project Setup

### Locally

```sh
npm install
npm run dev
```

### With Docker

```sh
# Dev server (vite)
docker build -t <image>:<tag> -f Dockerfile.dev .
docker run -p 5173:5173 <image>:<tag>

# Prod server (nginx)
docker build -t <image>:<tag> -f Dockerfile.prod .
docker run -p <host_port>:8080 <image>:<tag>  # Port forward to nginx
```

### Maintainers

{{cookiecutter.maintainer}}
