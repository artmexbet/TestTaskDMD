<script setup>

import Button from "primevue/button";
</script>

<template>
  <nav>
    <router-link to="/"><Button type="button" label="Список задач" /></router-link>
    <router-link :to="`/create-item`"><Button type="button" label="Добавить задачу" /></router-link>
  </nav>
</template>

<style scoped>
nav {
  display: flex;
  gap: 1rem;
}
</style>