import { useStores } from './use-stores'
import { getReasonPhrase } from 'http-status-codes'

export async function wrapper(callback, options) {
  // Manage loading state
  options.loading.value = true
  const res = await callback
  options.loading.value = false
  // Manage snackbar
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
}

function getText(res, options) {
  //  Define snackbar text priority:
  // 1. Custom Mapping
  // 2. API message
  // 3. HTTP status message from http-status-codes
  if ('mapping' in options && res.status in options.mapping) {
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
