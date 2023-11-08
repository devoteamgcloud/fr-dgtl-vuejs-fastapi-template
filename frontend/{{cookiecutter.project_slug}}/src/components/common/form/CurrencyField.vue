<template>
  <v-text-field 
    ref="inputRef"
    clearable
    :rules="rules"
    :label="label"
    class="pa-2"
  >
    <template
      v-if="$slots['append']"
      #append
    >
      <slot name="append" />
    </template>
  </v-text-field>
</template>
  
  <script setup lang="ts">
  import { watch } from "vue";
  import { CurrencyInputOptions, useCurrencyInput } from "vue-currency-input";
  
  const emit = defineEmits(["update:modelValue"]);
  
  const props = defineProps( {
    modelValue: {
      type: Number,
      required: true,
      default: 0,
    },
    rules: {
      type: Array[Function as any],
      default: () => []
    },
    label: {
      type: String,
      required: false,
      default: "Montant",
    },
    icon: {
      type: String,
      required: false,
      default: "mdi-currency-eur",
    },
    options: {
      type: Object as () => CurrencyInputOptions,
      required: false,
      default: () => (defaultOptions),
    }
  })
  
  // Merge specified options with default options
  // Use vue-currency-input directive
  const passedOptions = { ...defaultOptions, ...props.options };
  const { inputRef, numberValue, setValue, setOptions } = useCurrencyInput(passedOptions, false);
  
  watch(numberValue, function (value) {
    if (value) {
      emit('update:modelValue', value)
    } else {
      emit('update:modelValue', 0)
    }
  });

  watch(
    () => props.modelValue,
    (value) => {
      setValue(value)
    }
  )
  
  watch(
      () => props.options,
      (options) => {
        setOptions(options)
      }
    )

  </script>
  
  <script lang="ts">
    // cf. https://dm4t2.github.io/vue-currency-input/config.html
    const defaultOptions: CurrencyInputOptions = {
      currency: "EUR",
      locale: "fr-FR",
      autoDecimalDigits: false,
      precision: 2,
      valueRange: { min: 0, max: 2147483647 },
    };
  </script>
  