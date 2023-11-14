<template>
  <v-text-field
    :rules="rules"
    :label="$t(label) || label"
    :placeholder="$t(placeholder) || label"
    :density="density"
    clearable
    autocomplete="on"
    class="pa-2"
  >
    <template
      v-if="$slots['append']"
      #append
    >
      <slot name="append" />
    </template>
  </v-text-field>
</template>

<script setup lang="ts">
defineProps({
  rules: {
    type: Array[Function as any],
    default: () => []
  },
  label: {
    type: String,
    default: 'common.textField.label'
  },
  placeholder: {
    type: String,
    default: 'common.textField.placeholder'

  },
  density: {
    type: String as any,
    default: 'comfortable'
  }
})
</script>

<style scoped></style>
