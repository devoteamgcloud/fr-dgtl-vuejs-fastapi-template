import { Ref } from 'vue'

export const APISettings = {
  baseURL: import.meta.env.VITE_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json'
  }
}

export class SnackSettings {
  loading: Ref<boolean>             // Loading state for callback
  popup?: boolean                   // Show snackbar
  location?: string                 // Snackbar location (top, bottom, left, right, top right, top left, bottom right, bottom left)
  mapping?: Record<string, string>  // Custom mapping for snackbar text

  constructor(loading: Ref<boolean>, popup: boolean = true, location: string = 'top right', mapping: Record<string, string> = null) {
    this.loading = loading;
    this.popup = popup;
    this.location = location;
    if (!mapping) {
      delete this.mapping
    }
  }
}

export const TEST_PREFIX = 'quotes'
