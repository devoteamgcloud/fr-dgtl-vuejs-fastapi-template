<template>
  <v-container>
    <h2 class="text-center">
      Form & API call exemple
    </h2>
    <!-- Form Example -->
    <FormFields
      :id="1"
      clearable
      custom-actions
      @submit="showModal = true"
    >
      <template #body>
        <!-- TextField example -->
        <TextField
          v-model="usernameExample"
          :rules="[formValidation.fieldRequired(), formValidation.fieldMinLength(3)]"
          label="Username"
          prepend-inner-icon="mdi-account"
          class="mt-4"
        >
          <template #append>
            <v-alert
              type="info"
              variant="tonal"
            >
              Value: {% raw %}{{ usernameExample }}{% endraw %}
            </v-alert>
          </template>
        </TextField>

        <TextField
          v-model="emailExemple"
          :rules="[formValidation.fieldRequired(), formValidation.isEmail()]"
          label="Email"
          prepend-inner-icon="mdi-email"
        >
          <template #append>
            <v-alert
              type="info"
              variant="tonal"
            >
              Value: {% raw %}{{ emailExemple }} {% endraw %}
            </v-alert>
          </template>
        </TextField>

        <TextField
          v-model="passwordExemple"
          :rules="[formValidation.passwordRules()]"
          type="password"
          label="Password"
          prepend-inner-icon="mdi-lock"
        >
          <template #append>
            <v-alert
              type="info"
              variant="tonal"
            >
              Value: {% raw %}{{ passwordExemple }}{% endraw %}
            </v-alert>
          </template>
        </TextField>

        <!-- SelectField example -->
        <SelectField
          v-model="selectExemple"
          label="Select one state"
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
          @selection-updated="selectExemple = $event"
        >
          <template #append>
            <v-alert
              type="info"
              variant="tonal"
            >
              Value: {% raw %}{{ selectExemple }}{% endraw %}
            </v-alert>
          </template>
        </SelectField>

        <!-- AutocompleteField example -->
        <AutocompleteField
          v-model="autocompleteExemple"
          label="Select multiple states (autocomplete)"
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
          <template #append>
            <v-alert
              type="info"
              variant="tonal"
            >
              Value:
              <template v-if="autocompleteExemple.length > 0">
                {% raw %}{{ autocompleteExemple }}{% endraw %}
              </template>
            </v-alert>
          </template>
        </AutocompleteField>
        <FileField
          v-model="exampleFiles"
          label="Optional field"
          :multiple="true"
          clearable
          @file-change="exampleFiles = $event"
        />
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
          />
          <v-btn
            density="compact"
            icon="mdi-sync-circle"
            color="red"
            size="x-large"
            @click="clear"
          />
        </div>
      </template>
    </FormFields>

    <ModalContainer
      :model-value="showModal"
      main-title="Confirm?"
      @confirm="confirmSubmit()"
      @close="showModal = false"
    >
      <template #body>
        This will call a public API, are you sure?
      </template>
      <!-- Replace default actions if needed -->
      <!-- <template #customActions="{ confirm, close }">
        <v-btn @click="confirm()"></v-btn>
        <v-btn @click="close()"></v-btn>
      </template> -->
    </ModalContainer>

    <!-- Call API example -->
    <div
      v-if="loading"
      class="pa-8"
    >
      <div class="text-caption">
        Call in progress...
      </div>
      <v-progress-linear
        color="primary"
        indeterminate
        :height="5"
      />
    </div>
    <div
      v-else-if="apiResult.length > 0"
      class="d-flex justify-content-center flex-wrap"
    >
      <CardContainer
        v-for="entry in apiResult.slice(0, 3)"
        :key="entry.anime"
        :title="'Anime: ' + entry.anime"
      >
        <template #body>
          <div>
            "{% raw %}{{ entry.quote }}{% endraw %}"
          </div>
        </template>
        <template #footer>
          From {% raw %}{{ entry.character }}{% endraw %}
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
let apiResult = ref([] as any[])
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
