import { ref } from 'vue'
import { setActivePinia, createPinia } from 'pinia'
import { beforeEach, expect, test } from 'vitest'
import { SnackSettings } from '@/api/config'
import { wrapper } from '@/composables/use-api-wrapper'
import { useApis } from '@/composables/use-apis'

beforeEach(() => {
    // creates a fresh pinia and makes it active
    // Needed by useStores in wrapper
    setActivePinia(createPinia())
})

test('Test api-wrapper & apis composables', async () => {
    const apis = useApis()
    const loading = ref(false)
    const options = new SnackSettings(loading) // Default options
    const apiResult = await wrapper(apis.test.callExemple(), options) // May fail due to public API
    expect(apiResult).toBeInstanceOf(Array)
}, { timeout: 8000 })