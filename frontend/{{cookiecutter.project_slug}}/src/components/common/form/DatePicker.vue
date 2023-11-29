<template>
  <v-date-picker
    v-model="date"
    :min="props.min"
    :max="props.max"
    :allowed-dates="props.allowedDates"
    show-adjacent-months
    class="pa-2"
  >
    <template
      v-if="$slots.actions"
      #actions
    >
      <slot name="actions" />
    </template>
  </v-date-picker>
</template>

<script setup lang="ts">
const props = defineProps({
  modelValue: {
    type: Array[Date as any],
    default: null
  },
  min: {
    type: Date as any,
    default: null
  },
  max: {
    type: Date as any,
    default: null
  },
  allowedDates: {
    type: Function as any,
    default: null
  }
})

let date = props.modelValue
</script>
