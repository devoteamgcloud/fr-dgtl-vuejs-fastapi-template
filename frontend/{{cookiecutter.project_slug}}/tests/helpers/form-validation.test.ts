import { expect, test } from 'vitest'
import helpers from '@/helpers/form-validation'

test('Test required field', () => {
  expect(helpers.fieldRequired()('')).toBe('Field is required')
  expect(helpers.fieldRequired()(false)).toBe('Field is required')
  expect(helpers.fieldRequired()('test')).toBe(true)
  expect(helpers.fieldRequired()(true)).toBe(true)
})

test('Test minimal length field', () => {
  expect(helpers.fieldMinLength(5)('Nop')).toBe('Minimal length is 5')
  expect(helpers.fieldMinLength(5)('Valid input')).toBe(true)
})

test('Test maximal length field', () => {
  expect(helpers.fieldMaxLength(5)('Too long')).toBe('Maximal length is 5')
  expect(helpers.fieldMaxLength(5)('Ok')).toBe(true)
})

test('Test minimal value field', () => {
  expect(helpers.fieldMinValue(5)(4)).toBe('Minimal value is 5')
  expect(helpers.fieldMinValue(5)("4,95")).toBe('Minimal value is 5') // CurrencyField returns float string representation
  expect(helpers.fieldMinValue(5)(5)).toBe(true)
  expect(helpers.fieldMinValue(5)("5,95")).toBe(true)
})

test('Test maximal value field', () => {
  expect(helpers.fieldMaxValue(5)(6)).toBe('Maximal value is 5')
  expect(helpers.fieldMaxValue(5)("6,95")).toBe('Maximal value is 5')
  expect(helpers.fieldMaxValue(5)(5)).toBe(true)
  expect(helpers.fieldMaxValue(5)("4,95")).toBe(true)
})

test('Test e-mail field', () => {
  expect(helpers.isEmail()('test')).toBe('E-mail must be valid')
  expect(helpers.isEmail()('test@gmail.com')).toBe(true)
})

test('Test password field', () => {
  expect(helpers.passwordRules()('Not valid')).toBe('Password must contain at least 8 characters, one letter and one number (no spaces)')
  expect(helpers.passwordRules()('Validpassw0rd')).toBe(true)
})