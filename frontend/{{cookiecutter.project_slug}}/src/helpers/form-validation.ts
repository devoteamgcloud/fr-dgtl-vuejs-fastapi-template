import { i18n } from '@/main.ts'

export default {
  fieldRequired() {
    return (value) => !!value || (!!value && value.length > 0) || i18n.global.t('form.required')
  },

  fieldMinLength(size: number) {
    return (value) => value.length >= size || i18n.global.t('form.minimalLength', { length: size })
  },

  fieldMaxLength(size: number) {
    return (value) => value.length <= size || i18n.global.t('form.maximalLength', { length: size })
  },

  fieldMinValue(size: number) {
    return function asNumber(value) {
      if (typeof value === 'number') {
        return value >= size || 'Minimal value is ' + size
      }
      return Number.parseFloat(value.replaceAll(',', '.')) >= size || i18n.global.t('form.minimalValue', { value: size })
    }
  },

  fieldMaxValue(size: number) {
    return function asNumber(value) {
      if (typeof value === 'number') {
        return value <= size || 'Maximal value is ' + size
      }
      return Number.parseFloat(value.replaceAll(',', '.')) <= size || i18n.global.t('form.maximalValue', { value: size })
    }
  },

  isEmail() {
    return (value) => /.+@.+\..+/.test(value) || i18n.global.t('form.emailNotValid')
  },

  passwordRules() {
    return (value) => /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(value) || i18n.global.t('form.passwordRequirements')
  }
}
