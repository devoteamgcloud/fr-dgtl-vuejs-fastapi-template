<template>
  <v-autocomplete
    :label="label || 'Autocomplete'"
    :items="props.items"
    :itemValue="props.itemValue"
    :itemTitle="props.itemTitle"
    :multiple="props.multiple"
    :chips="props.chips"
    class="pa-2"
  >
    <template v-slot:append>
      <slot v-if="$slots['append']" name="append"></slot>
    </template>
  </v-autocomplete>
</template>

<script setup lang="ts">
const props = defineProps({
  label: {
    type: String,
    default: ''
  },
  items: {
    type: Array,
    required: true
  },
  itemTitle: {
    type: String,
    default: 'title'
  },
  itemValue: {
    type: String,
    default: 'value'
  },
  multiple: {
    type: Boolean,
    default: false
  },
  chips: {
    type: Boolean,
    default: false
  }
})
</script>
