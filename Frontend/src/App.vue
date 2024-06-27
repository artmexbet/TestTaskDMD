<script setup>

</script>

<template>
  <div>
    <router-link to="/">Items List</router-link>
    <router-link :to="`/create-item`">Add item</router-link>
  </div>
  <br>
  <router-view/>
</template>

<style scoped>

</style>
