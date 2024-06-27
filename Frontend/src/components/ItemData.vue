<script setup>
import {ref, watchEffect} from "vue";
import ProgressSpinner from 'primevue/progressspinner';


const props = defineProps({
  item: Object
});

// Эта переменная является прокинутой из ItemsList информацией о задаче
const item = ref(props.item);
const task = ref(null);

const is_loading = ref(false);

const loadItem = async () => {
  const response = await fetch(`http://localhost:8000/api/tasks/${item.value['key']}`);
  is_loading.value = true;
  const data = await response.json();
  is_loading.value = false;
  return data;
};


watchEffect(() => {
  item.value = props.item;
  if (props.item) {
    loadItem().then(data => {
      task.value = data;
      console.log('task', task.value);
    });
  }
});
</script>

<template>
  <div v-if="task">
    <h2>{{ task.name }}</h2>
    <p>{{ task.description }}</p>
  </div>
  <div v-else-if="is_loading">
    <ProgressSpinner class="loading"/>
  </div>
  <div v-else>
    <p>Выберите задачу</p>
  </div>
</template>

<style scoped>
.loading {
  margin: 0 auto;
  display: block;
}
</style>