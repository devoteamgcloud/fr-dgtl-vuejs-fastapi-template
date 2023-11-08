export default {
  fieldRequired() {
    return (value) => !!value || (!!value && value.length > 0) || 'Field is required'
  },

  fieldMinLength(size: number) {
    return (value) => value.length >= size || 'Minimal length is ' + size
  },

  fieldMaxLength(size: number) {
    return (value) => value.length <= size || 'Maximal length is ' + size
  },

  fieldMinValue(size: number) {
    return function asNumber(value) {
      if (typeof value === 'number') {
        return value >= size || 'Minimal value is ' + size
      }
      return Number.parseFloat(value.replaceAll(',', '.')) >= size || 'Minimal value is ' + size
    }
  },

  fieldMaxValue(size: number) {
    return function asNumber(value) {
      if (typeof value === 'number') {
        return value <= size || 'Maximal value is ' + size
      }
      return Number.parseFloat(value.replaceAll(',', '.')) <= size || 'Maximal value is ' + size
    }
  },

  isEmail() {
    return (value) => /.+@.+\..+/.test(value) || 'E-mail must be valid'
  },

  passwordRules() {
    return (value) => /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(value) || 'Password must contain at least 8 characters, one letter and one number (no spaces)'
  }
}
