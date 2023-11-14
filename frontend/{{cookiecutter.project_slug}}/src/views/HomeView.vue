<template>
  <v-container>
    <h2 class="text-center">
      {% raw %}{{ $t('homeView.formTitle') }}{% endraw %}
    </h2>
    <!-- Form Example -->
    <FormField
      :id="1"
      clearable
      custom-actions
      @submit="showModal = true"
    >
      <template #body>
        <!-- DatePicker exemple WIP (Waiting v3.4.0) -->
        <!-- <DatePicker
          v-model="dateExemple"
          class="float-left mx-6"
        /> -->
        <v-row>
          <v-col cols="6">
            <!-- TextField example -->
            <TextField
              v-model="usernameExample"
              :rules="[formValidation.fieldRequired(), formValidation.fieldMinLength(3)]"
              :label="$t('homeView.usernameField.label')"
              :placeholder="$t('homeView.usernameField.placeholder')"
              prepend-inner-icon="mdi-account"
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
          </v-col>
          <v-col cols="6">
            <TextField
              v-model="emailExemple"
              :rules="[formValidation.fieldRequired(), formValidation.isEmail()]"
              :label="$t('common.emailField.label')"
              :placeholder="$t('common.emailField.placeholder')"
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
          </v-col>
        </v-row>
        <v-row>
          <TextField
            v-model="passwordExemple"
            :rules="[formValidation.passwordRules()]"
            type="password"
            :label="$t('common.passwordField.label')"
            :placeholder="$t('common.passwordField.placeholder')"
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
        </v-row>
        <v-row>
          <!-- CurrencyField example -->
          <CurrencyField
            v-model="currencyExemple"
            :options="{ currency: 'EUR', valueRange: { min: 1, max: 10 }}"
            :rules="[formValidation.fieldRequired(), formValidation.fieldMinValue(1), formValidation.fieldMaxValue(10)]"
            prepend-inner-icon="mdi-currency-eur"
            class="mt-4"
          >
            <template #append>
              <v-alert
                type="info"
                variant="tonal"
              >
                Value: {% raw %}{{ currencyExemple }}{% endraw %}
              </v-alert>
            </template>
          </CurrencyField>
        </v-row>
        <v-row>
          <v-col cols="6">
            <!-- SelectField example -->
            <SelectField
              v-model="selectExemple"
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
          </v-col>
          <v-col cols="6">
            <!-- AutocompleteField example -->
            <AutocompleteField
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
          </v-col>
        </v-row>
        <v-row>
          <FileField
            v-model="exampleFiles"
            :multiple="true"
            clearable
            @file-change="exampleFiles = $event"
          />
        </v-row>
        <v-row>
          <SwitchField
            v-model="switchExemple"
            :rules="[formValidation.fieldRequired()]"
            @change="switchExemple = $event"
          >
            <template
              v-if="switchExemple"
              #label
            >
              Fake progress
              <v-progress-circular
                indeterminate
                color="secondary"
                size="24"
                class="ms-2"
              />
            </template>
            <template #append>
              <v-alert
                type="info"
                variant="tonal"
              >
                Value: {% raw %}{{ switchExemple }}{% endraw %}
              </v-alert>
            </template>
          </SwitchField>
        </v-row>
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
    </FormField>

    <ModalContainer
      :model-value="showModal"
      @confirm="confirmSubmit()"
      @close="showModal = false"
    >
      <template #body>
        {% raw %}{{ $t('homeView.modalBody') }}{% endraw %}
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
      class="mt-8"
    >
      <hr>
      <div class="d-flex justify-content-center flex-wrap">
        <CardContainer
          v-for="entry in apiResult.slice(0, 3)"
          :key="entry.anime"
          :title="'Anime: ' + entry.anime"
        >
          <template #body>
            <div>"{% raw %}{{ entry.quote }}{% endraw %}"</div>
          </template>
          <template #footer>
            From {% raw %}{{ entry.character }}{% endraw %}
          </template>
        </CardContainer>
      </div>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import CardContainer from '@/components/common/CardContainer.vue'
import AutocompleteField from '@/components/common/form/AutocompleteField.vue'
import FormField from '@/components/common/form/FormField.vue'
import FileField from '@/components/common/form/FileField.vue'
import ModalContainer from '@/components/common/ModalContainer.vue'
import TextField from '@/components/common/form/TextField.vue'
import SwitchField from '@/components/common/form/SwitchField.vue'
import SelectField from '@/components/common/form/SelectField.vue'
import CurrencyField from '@/components/common/form/CurrencyField.vue'
// import DatePicker from '@/components/common/form/DatePicker.vue'
import formValidation from '@/helpers/form-validation'
import { SnackSettings } from '@/api/config'
import { ref } from 'vue'
import { useApis } from '@/composables/use-apis'
import { wrapper } from '@/composables/use-api-wrapper'

const apis = useApis()
let apiResult = ref([] as any[])
let loading = ref(false)
// let dateExemple = ref(null as any)

let usernameExample = ref('')
let emailExemple = ref('')
let passwordExemple = ref('')
let currencyExemple = ref(0)
let switchExemple = ref(false)
let selectExemple = ref(null as any)
let autocompleteExemple = ref([])
let exampleFiles = ref([])
let showModal = ref(false)

function confirmSubmit() {
  showModal.value = false
  callTestApi()
}

async function callTestApi() {
  const options = new SnackSettings(true, 'bottom', {
    200: 'Public API called with success',
    400: 'Error from client',
    500: 'Error from server'
  })
  apiResult.value = await wrapper(apis.test.callExemple(), loading, options)
}
</script>

<style scoped>
.v-date-picker {
  padding: 0 !important;
}
.text-info {
  padding: 5px !important
}
</style>