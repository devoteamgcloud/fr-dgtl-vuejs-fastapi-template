<template>
  <v-file-input
    :accept="accept"
    :label="label"
    :multiple="multiple"
    :rules="rules"
    show-size
    prepend-inner-icon="mdi-paperclip"
    :prepend-icon="null"
    class="pa-2"
    @update:model-value="$emit('fileChange', $event)"
  >
    <template #selection="{ fileNames }">
      <div v-if="multiple">
        <template
          v-for="(fileName, index) in fileNames"
          :key="fileName"
        >
          <v-chip
            v-if="index < 2"
            label
            class="me-2"
          >
            {% raw %}{{ fileName }}{% endraw %}
          </v-chip>
          <span v-else-if="index === 2"> {% raw %} +{{ files.length - 2 }} {% endraw %} File(s) </span>
        </template>
      </div>
    </template>
  </v-file-input>
</template>
  
  <script setup lang="ts">
  import { ref } from 'vue'

  defineEmits(['fileChange'])

  const props = defineProps({
    modelValue: {
      type: Array<File>,
      default: () => []
    },
    rules: {
      type: Array[Function as any],
      default: () => []
    },
    accept: {
      type: String,
      default: 'img/*'
    },
    label: {
      type: String,
      default: 'Select file'
    },
    multiple: {
      type: Boolean,
      default: false
    }
  })
  
  let files = ref(props.modelValue)
  </script>
  
  <style scoped></style>
  