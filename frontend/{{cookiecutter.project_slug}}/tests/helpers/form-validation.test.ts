import { expect, test } from 'vitest'
import helpers from '@/helpers/form-validation'

test('Test required field', () => {
  expect(helpers.fieldRequired()('')).toBe('Field is required')
  expect(helpers.fieldRequired()('test')).toBe(true)
})

test('Test minimal length field', () => {
  expect(helpers.fieldMinLength(5)('Nop')).toBe('Minimal length is 5')
  expect(helpers.fieldMinLength(5)('Valid input')).toBe(true)
})

test('Test maximal length field', () => {
  expect(helpers.fieldMaxLength(5)('Too long')).toBe('Maximal length is 5')
  expect(helpers.fieldMaxLength(5)('Ok')).toBe(true)
})

test('Test e-mail field', () => {
  expect(helpers.isEmail()('test')).toBe('E-mail must be valid')
  expect(helpers.isEmail()('test@gmail.com')).toBe(true)
})

test('Test password field', () => {
  expect(helpers.passwordRules()('Not valid')).toBe('Password must contain at least 8 characters, one letter and one number (no spaces)')
  expect(helpers.passwordRules()('Validpassw0rd')).toBe(true)
})