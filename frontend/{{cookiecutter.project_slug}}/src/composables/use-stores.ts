import { snackStore } from '@/stores/snackbar'

export function useStores() {
  const snack = snackStore()
  return { snack }
}
