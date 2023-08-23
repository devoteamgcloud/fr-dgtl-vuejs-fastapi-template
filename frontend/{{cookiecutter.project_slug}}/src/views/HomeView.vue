<template>
  <v-container>
    <h2 class="text-center">Form & API call exemple</h2>
    <!-- Form Example -->
    <FormFields :id="1" clearable custom-actions @submit="showModal = true">
      <template #body>
        <!-- TextField example -->
        <TextField
          v-model="usernameExample"
          :rules="[formValidation.fieldRequired(), formValidation.fieldMinLength(3)]"
          label="Username"
          prepend-inner-icon="mdi-account"
          class="mt-4"
        >
          <template v-slot:append>
            {% raw %}
            <v-alert type="info" variant="tonal"> Value: {{ usernameExample }}</v-alert>
            {% endraw %}
          </template>
        </TextField>

        <TextField
          v-model="emailExemple"
          :rules="[formValidation.fieldRequired(), formValidation.isEmail()]"
          label="Email"
          prepend-inner-icon="mdi-email"
        >
          <template v-slot:append>
            {% raw %}
            <v-alert type="info" variant="tonal"> Value: {{ emailExemple }}</v-alert>
            {% endraw %}
          </template>
        </TextField>

        <TextField
          v-model="passwordExemple"
          :rules="[formValidation.passwordRules()]"
          type="password"
          label="Password"
          prepend-inner-icon="mdi-lock"
        >
          <template v-slot:append>
            {% raw %}
            <v-alert type="info" variant="tonal"> Value: {{ passwordExemple }}</v-alert>
            {% endraw %}
          </template>
        </TextField>

        <!-- SelectField example -->
        <SelectField
          label="Select one state"
          :v-model="selectExemple"
          :rules="[formValidation.fieldRequired()]"
          :items="[
            { state: 'Florida', abbr: 'FL' },
            { state: 'Georgia', abbr: 'GA' },
            { state: 'Nebraska', abbr: 'NE' },
            { state: 'California', abbr: 'CA' },
            { state: 'New York', abbr: 'NY' }
          ]"
          item-title="state"
          item-value="abbr"
          :multiple="false"
          :chips="true"
          closable-chips
          prepend-inner-icon="mdi-flag"
          @selectionUpdated="selectExemple = $event"
        >
          <template v-slot:append>
            {% raw %}
            <v-alert type="info" variant="tonal"> Value: {{ selectExemple }}</v-alert>
            {% endraw %}
          </template>
        </SelectField>

        <!-- AutocompleteField example -->
        <AutocompleteField
          label="Select multiple states (autocomplete)"
          v-model="autocompleteExemple"
          :rules="[formValidation.fieldRequired(), formValidation.fieldMaxLength(2)]"
          :items="[
            { title: 'Florida', value: 'FL' },
            { title: 'Georgia', value: 'GA' },
            { title: 'Nebraska', value: 'NE' },
            { title: 'California', value: 'CA' },
            { title: 'New York', value: 'NY' }
          ]"
          :multiple="true"
          :chips="true"
          closable-chips
          prepend-inner-icon="mdi-city"
        >
          <template v-slot:append>
            {% raw %}
            <v-alert type="info" variant="tonal">
              Value:
              <template v-if="autocompleteExemple.length > 0">
                {{ autocompleteExemple }}
              </template>
            </v-alert>
            {% endraw %}
          </template>
        </AutocompleteField>
        <FileField
          v-model="exampleFiles"
          label="Optional field"
          :multiple="true"
          clearable
          @fileChange="exampleFiles = $event"
        >
        </FileField>
      </template>
      <!-- Replace default actions when custom-actions props is passed -->
      <template #actions="{ validate, clear }">
        <div class="d-flex justify-space-evenly">
          <v-btn
            density="compact"
            icon="mdi-check-circle-outline"
            color="green"
            size="x-large"
            @click="validate"
          >
          </v-btn>
          <v-btn density="compact" icon="mdi-sync-circle" color="red" size="x-large" @click="clear">
          </v-btn>
        </div>
      </template>
    </FormFields>

    <ModalContainer
      :model-value="showModal"
      main-title="Confirm?"
      @confirm="confirmSubmit()"
      @close="showModal = false"
    >
      <template #body> This will call a public API, are you sure? </template>
      <!-- Replace default actions if needed -->
      <!-- <template #customActions="{ confirm, close }">
        <v-btn @click="confirm()"></v-btn>
        <v-btn @click="close()"></v-btn>
      </template> -->
    </ModalContainer>

    <!-- Call API example -->
    <div v-if="loading" class="pa-8">
      <div class="text-caption">Call in progress...</div>
      <v-progress-linear color="primary" indeterminate :height="5"></v-progress-linear>
    </div>
    <div v-else-if="apiResult.count" class="d-flex justify-content-center flex-wrap">
      <CardContainer
        :key="entry.API"
        v-for="entry in apiResult.entries.slice(0, 3)"
        :title="entry.API"
      >
        <template v-slot:body>
          <div>
            {% raw %}
            {{ entry.Description }}
            {% endraw %}
          </div>
        </template>
        <template v-slot:footer>
          {% raw %}
          {{ entry.Category }}
          {% endraw %}
        </template>
      </CardContainer>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import CardContainer from '@/components/common/CardContainer.vue'
import { useApis } from '@/composables/use-apis'
import { wrapper } from '@/composables/use-api-wrapper'
import TextField from '@/components/common/form/TextField.vue'
import SelectField from '@/components/common/form/SelectField.vue'
import formValidation from '@/helpers/form-validation'
import { ApiResponseSettings } from '@/api/config'
import { ref } from 'vue'
import AutocompleteField from '@/components/common/form/AutocompleteField.vue'
import FormFields from '@/components/common/form/FormFields.vue'
import FileField from '@/components/common/form/FileField.vue'
import ModalContainer from '@/components/common/ModalContainer.vue'

const apis = useApis()
let apiResult = ref({ count: 0, entries: [] })
let loading = ref(false)

let usernameExample = ref('')
let emailExemple = ref('')
let passwordExemple = ref('')
let selectExemple = ref(null as any)
let autocompleteExemple = ref([])
let exampleFiles = ref([])
let showModal = ref(false)

function confirmSubmit() {
  showModal.value = false
  callTestApi()
}

async function callTestApi() {
  let options: ApiResponseSettings = {
    loading: loading,
    popup: true,
    location: 'top right',
    mapping: {
      200: 'Custom success message'
    }
  }

  apiResult.value = await wrapper(apis.test.callExemple(), options)
}
</script>
