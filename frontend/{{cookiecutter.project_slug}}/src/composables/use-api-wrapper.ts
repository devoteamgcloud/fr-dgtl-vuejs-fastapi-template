import { Ref } from 'vue'
import { useStores } from './use-stores'
import { getReasonPhrase } from 'http-status-codes'
import { SnackSettings } from '@/api/config'

export async function wrapper(callback, loading: Ref<boolean>, options = null) {
  const { snack } = useStores()
  if (!options) {
    options = new SnackSettings(true, 'top right', null)
  }
  loading.value = true
  try {
    const res = await callback
    if (options.popup) {
      const { snack } = useStores()
      snack.display({
        text: getText(res, options),
        type: getType(res.status),
        icon: getIcon(res.status),
        location: options.location || 'bottom'
      })
    }
    return res.data
  } catch (res) {
    if (options.popup) {
      snack.display({
        text: res.message,
        type: 'error',
        icon: getIcon(null),
        location: options.location || 'bottom'
      })
      return []
    }
  } finally {
    loading.value = false
  }
}

function getText(res, options) {
  // Define snackbar text priority:
  // 1. Custom Mapping
  // 2. API 'message' key
  // 3. HTTP status message from http-status-codes
  if (options.mapping && res.status in options.mapping) {
    return options.mapping[res.status]
  }
  return res.data?.message || `${res.status}: ${getReasonPhrase(res.status)}`
}

function getType(status) {
  switch (status) {
    case 200:
    case 201:
    case 202:
    case 204:
      return 'success'
    case 400:
      return 'warning'
    default:
      return 'error'
  }
}

function getIcon(status) {
  switch (status) {
    case 200:
    case 201:
    case 202:
    case 204:
      return 'mdi-check-circle'
    case 400:
      return 'mdi-message-alert'
    default:
      return 'mdi-alert'
  }
}
