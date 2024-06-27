<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import ItemsList from "@/components/ItemsList.vue";
</script>

<template>
  <header>
    <ItemsList />
  </header>

  <main>
<!--    <TheWelcome />-->
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
