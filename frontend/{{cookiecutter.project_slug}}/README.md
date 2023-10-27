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

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Maintainers

{{cookiecutter.maintainer}}
