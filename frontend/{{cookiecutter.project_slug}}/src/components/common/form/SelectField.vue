<template>
  <v-select
    v-model="selectedItems"
    @update:modelValue="$emit('selectionUpdated', $event)"
    :label="label"
    :items="props.items"
    :itemValue="props.itemValue"
    :itemTitle="props.itemTitle"
    :multiple="multiple"
    :chips="showAsChips"
    class="pa-2"
  >
    <template v-slot:prepend-item>
      <div v-if="multiple">
        <v-list-item :title="`Select All (${selectedItems.length})`" @click="selectAll">
          <template v-slot:prepend>
            <v-checkbox-btn
              :color="selectedSome ? 'indigo-darken-4' : undefined"
              :indeterminate="selectedSome && !selectedAll"
              :model-value="selectedSome"
            ></v-checkbox-btn>
          </template>
        </v-list-item>

        <v-divider class="mt-2"></v-divider>
      </div>
    </template>

    <template v-slot:append>
      <slot v-if="$slots['append']" name="append"></slot>
    </template>
  </v-select>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

const props = defineProps({
  modelValue: {
    type: String || Array
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
  label: {
    type: String,
    default: 'Select items'
  },
  density: {
    type: String as any,
    default: 'comfortable'
  },
  showAsChips: {
    type: Boolean,
    default: false
  }
})

let selectedItems = ref(props.modelValue)

const selectedAll = computed(() => {
  return selectedItems.value.length === props.items.length
})

const selectedSome = computed(() => {
  return selectedItems.value.length > 0
})

function selectAll() {
  if (selectedAll.value) {
    selectedItems.value = []
  } else {
    selectedItems.value = props.items.slice()
  }
}
</script>

<style scoped></style>
