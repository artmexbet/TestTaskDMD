<script setup>
import {ref, watchEffect} from "vue";

const props = defineProps({
  task: Object
});

console.log(props.task);
// Эта переменная является прокинутой из ItemsList информацией о задаче
const task = ref(props.task);

watchEffect(() => {
  task.value = props.task;
});
</script>

<template>
  <h2>{{ task.name }}</h2>
  <p>{{ task.description }}</p>
  <p>Исполнители: {{ task.performers }}</p>
  <p>Статус: {{ task.status }}</p>
  <p>Запланированное время: {{ task.planned_effort }}</p>
  <p>Фактическое время: {{ task.actual_effort }}</p>
  <p>Дата окончания: {{ task.completion_date }}</p>
</template>

<style scoped>

</style>