
<template>
  <v-container>
    <ServerTable
      :headers="headers"
      :items="apiResult"
      :loading="loading"
      :total-items="apiResult.length"
      @update-data="fetchData($event)"
    />
  </v-container>
</template>

<script setup lang="ts">
import { useApis } from '@/composables/use-apis.ts';
import { ref } from 'vue';
import { wrapper } from '@/composables/use-api-wrapper.ts';
import ServerTable from '@/components/common/ServerTable.vue';

const apis = useApis()

const headers = [
  { title: 'Anime', value: 'anime', align: 'center', sortable: true },
  { title: 'Character', value: 'character', align: 'center', sortable: true },
  { title: 'Quote', value: 'quote', align: 'center', sortable: true },
]
const totalItems = ref(0)

const loading = ref(false)
let apiResult = ref([] as any[])

async function fetchData(options) {
  const { page, itemsPerPage, sortBy, groupBy, search } = options
  console.log(page, itemsPerPage, sortBy, groupBy, search)   // Use this to paginate if API supports it

  apiResult.value = await wrapper(apis.test.callExemple(), loading, { show: false })
  totalItems.value = apiResult.value.length

}

</script>