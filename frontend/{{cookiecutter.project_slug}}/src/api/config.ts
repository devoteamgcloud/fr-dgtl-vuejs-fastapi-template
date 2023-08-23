import { Ref } from 'vue'

export const APISettings = {
  baseURL: import.meta.env.VITE_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json'
  }
}

export interface ApiResponseSettings {
  loading: Ref<boolean> // Loading state for callback
  popup?: boolean // Show snackbar
  location?: string // Snackbar location (top, bottom, left, right, top right, top left, bottom right, bottom left)
  mapping?: Record<string, string> // Custom mapping for snackbar text
}

export const TEST_PREFIX = 'entries'
