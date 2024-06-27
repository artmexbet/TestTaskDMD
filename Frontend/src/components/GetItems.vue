<script setup>
import ItemsList from "@/components/ItemsList.vue";
import ItemData from "@/components/ItemData.vue";
import {ref} from "vue";

const selectedItem = ref(null);
const handleSelectedItem = (node) => {
  selectedItem.value = node;
};

</script>

<template>
  <header>
    <ItemsList @selected-item="handleSelectedItem"/>
  </header>

  <main>
    <ItemData :item="selectedItem"/>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: start;
    flex-direction: column;
    padding-right: calc(var(--section-gap) / 2);
  }
}
</style>
