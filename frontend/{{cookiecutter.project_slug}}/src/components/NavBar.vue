<template>
  <v-app-bar
    id="navbar"
    app
    :height="'--navigation-bar-height'"
    dark
  >
    <h3 class="ml-4">
      {{ cookiecutter.project_name }}
    </h3>
    <v-app-bar-nav-icon />
    <v-spacer />
    <v-btn @click="prefStore.toggleTheme(theme)">
      <v-icon
        v-if="prefStore.isDark"
        icon="fa:fa fa-moon"
      />
      <v-icon
        v-else
        icon="fa:fa fa-sun"
      />
    </v-btn>
  </v-app-bar>
</template>

<script setup lang="ts">
import { useTheme } from 'vuetify'
import { preferencesStore } from '@/stores/preferences'
import { onMounted } from 'vue'

const theme = useTheme()
const prefStore = preferencesStore()

onMounted(() => {
  theme.global.name.value = prefStore.isDark ? 'customDarkTheme' : 'customLightTheme'
})
</script>

<style scoped>
#navbar {
  height: var(--navigation-bar-height);
}
</style>
