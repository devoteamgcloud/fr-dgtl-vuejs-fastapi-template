import { expect, test } from 'vitest'
import example from '@/api/example'

test('Test example API call', async () => {
    await expect(example.callExemple()).resolves.toBeTruthy()
}, { timeout: 8000 })