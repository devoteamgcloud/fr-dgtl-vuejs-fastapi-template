import { defineStore } from 'pinia'

export const preferencesStore = defineStore({
  id: 'preferences',
  state: (): any => ({
    isDark: true,
    locale: 'en'
  }),
  actions: {
    toggleTheme(theme) {
      this.isDark = !this.isDark
      theme.global.name.value = this.isDark ? 'customDarkTheme' : 'customLightTheme'
    }
  },
  persist: true
})
