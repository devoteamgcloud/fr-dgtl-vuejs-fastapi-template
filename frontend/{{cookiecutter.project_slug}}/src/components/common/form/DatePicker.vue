<template>
  <v-menu
    v-model="showPicker"
    transition="scale-transition"
    :close-on-content-click="false"
    offset-y
  >
    <template #activator="scopeData">
      <v-text-field
        v-model="dateFormatted"
        :label="$t(props.label)"
        prepend-inner-icon="mdi-calendar"
        readonly
        v-bind="scopeData.props"
      />
    </template>
    
    <v-date-picker
      v-model="innerDate"
      :locale="prefStore.locale"
      :color="props.color"
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
  </v-menu>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useDate } from 'vuetify'
import { preferencesStore } from '@/stores/preferences'

const date = useDate()
const prefStore = preferencesStore()

const props = defineProps({
  modelValue: {
    type: Array[Date as any],
    default: null
  },
  label: {
    type: String,
    default: 'common.datePickerField.label'
  },
  color: {
    type: String,
    default: 'red'
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

let innerDate = ref(props.modelValue)
let showPicker = ref(false)

const dateFormatted = computed(() => {
  if (innerDate.value) {
    return date.format(innerDate.value, 'DD/MM/YYYY')
  }
  return ''
})
</script>
