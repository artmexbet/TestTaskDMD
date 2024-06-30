<script setup>
import {ref, watchEffect} from "vue";
import ProgressSpinner from 'primevue/progressspinner';
import CheckData from "@/components/CheckData.vue";
import EditTask from "@/components/EditTask.vue";
import Button from "primevue/button";
import axios from "axios";
import Toast from "primevue/toast";

import {useToast} from 'primevue/usetoast';
import { serverUrl } from '../config';

const toast = useToast();

const props = defineProps({
  item: Object
});

// Эта переменная является прокинутой из ItemsList информацией о задаче
const item = ref(props.item);
const task = ref(null);

const is_loading = ref(false);

const loadTasks = () => {
  is_loading.value = true;
  axios.get(`${serverUrl}/tasks/${item.value['key']}`).then(
      (response) => {
        task.value = response.data;
        is_loading.value = false;
      }
  );
}

watchEffect(() => {
  item.value = props.item;
  if (props.item) {
    loadTasks();
  }
});

const isEditing = ref(false);

const deleteTask = () => {
  axios.delete(`${serverUrl}/tasks/${task.value.id}/`).then(
      () => {
        task.value = null;
        toast.add({severity: 'success', summary: 'Удаление задания', detail: 'Задание успешно удалено', life: 3000});
        loadTasks();
      }
  );
};

</script>

<template>
  <Toast/>
  <div v-if="task">
    <div v-if="isEditing">
      <EditTask :task="task"/>
      <Button type="button" label="Отмена" @click="isEditing = false"/>
    </div>
    <div v-else>
      <CheckData :task="task"/>
      <div>
        <Button type="button" label="Редактировать" @click="isEditing = true" severity="info" class="button-spacing"/>
        <Button type="button" label="Удалить" @click="deleteTask" severity="danger" class="button-spacing"/>
      </div>
    </div>
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

.button-spacing{
  margin-right: 10px;
}
</style>