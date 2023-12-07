<template>
  <v-container>
    <v-data-table-server
      v-model:items-per-page="itemsPerPage"
      :headers="headers"
      :items-length="totalItems"
      :items="items"
      :loading="loading"
      :search="search"
      return-object
      @update:options="fetchData($event)"
    />
  </v-container>
</template>
    
<script setup lang="ts">
import {  ref } from 'vue'
const emit = defineEmits(['updateData'])

defineProps({
  headers: {
      type: Array<Object>,
      default: []
  },
  items: {
      type: Array<Object>,
      default: []
  },
  loading: {
      type: Boolean,
      default: false
  },
  totalItems: {
      type: Number,
      default: 0
  },
  search: {
      type: String,
      default: ''
  }
})

let itemsPerPage = ref(10)

function fetchData(options) {
  const { page, itemsPerPage, sortBy, groupBy, search } = options
  emit('updateData', { page, itemsPerPage, sortBy, groupBy, search })
}
</script>