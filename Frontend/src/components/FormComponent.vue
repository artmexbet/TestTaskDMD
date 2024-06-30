<script setup>
import {onMounted, ref, watchEffect} from 'vue';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Listbox from 'primevue/listbox';
import TreeSelect from "primevue/treeselect";
import Button from 'primevue/button';
import axios from "axios";
import Toast from "primevue/toast";

// Создаём уведомление об успешном сохранении
import {useToast} from 'primevue/usetoast';

const toast = useToast();

const showSuccess = () => {
  toast.add({severity: 'success', summary: 'Добавление задания', detail: 'Задание успешно добавлено', life: 3000});
};

const showError = (e) => {
  toast.add({severity: 'error', summary: 'Ошибка', detail: e, life: 3000});
};

// Создаём форму и заполняем её данными
const form = ref({
  name: '',
  description: '',
  performers: '',
  status: '',
  planned_effort: '',
  actual_effort: '',
  parent_task: null,
});

const statuses = ref([
  {label: 'Назначена', value: 'assigned'},
  {label: 'Выполняется', value: 'in_progress'},
  {label: 'Приостановлена', value: 'paused'},
  {label: 'Завершена', value: 'completed'},
]);
const requiredFields = ['name', 'performers', 'status', 'planned_effort'];

const submitForm = () => {
  // Простая валидация
  for (let i = 0; i < requiredFields.length; i++) {
    if (!form.value[requiredFields[i]]) {
      showError(`Пожалуйста, заполните поле ${requiredFields[i]}`);
      return;
    }
  }
  console.log(selectedNode.value);
  if (selectedNode.value === undefined) {
    form.value['parent_task'] = null;
  } else {
    form.value['parent_task'] = selectedNode.value['key'];
  }

  form.value['actual_effort'] = form.value['planned_effort'];

  axios.post('http://localhost:8000/api/tasks/', form.value)
      .then(() => {
        error.value = '';
        form.value = {
          name: '',
          description: '',
          performers: '',
          status: '',
          planned_effort: '',
          actual_effort: '',
          parent_task: null,
        };
        fetchTasks();
      })
      .catch((e) => {
        showError(e.response.data)
      });
};

const nodes = ref(null);
const selectedNode = ref(null);

const onNodeSelected = (node) => {
  selectedNode.value = node;
};

// Получаем список задач для выбора родительской задачи
const fetchTasks = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/tasks/');
    nodes.value = response.data;
  } catch (e) {
    console.error(e);
  }
};

onMounted(fetchTasks);
</script>

<template>
  <Toast/>
  <form @submit.prevent="submitForm">
    <div>
      <label for="name">Название задачи</label>
      <InputText id="name" v-model="form.name"/>
    </div>
    <div>
      <label for="description">Описание</label>
      <Textarea id="description" v-model="form.description"/>
    </div>
    <div>
      <label for="performers">Исполнители</label>
      <InputText id="performers" v-model="form.performers"/>
    </div>
    <div>
      <label for="status">Статус</label>
      <Listbox id="status" v-model="form.status" :options="statuses" option-label="label" option-value="value"/>
    </div>
    <div>
      <label for="planned_effort">Планируемое время выполнения</label>
      <InputText id="planned_effort" v-model="form.planned_effort"/>
    </div>
    <div>
      <label for="parent_task">Задание-родитель</label>
      <p>{{task}}</p>
      <TreeSelect @node-select="onNodeSelected" :options="nodes" :selection-mode="single" :style="{width: '100%'}"/>
    </div>
    <Button type="submit" label="Подтвердить"/>
  </form>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

input, textarea, .p-dropdown, .p-listbox {
  width: 100%;
  padding: 0.5rem;
  border-radius: 0.5rem;
  border: 1px solid #ccc;
}

.error {
  color: red;
  margin-bottom: 1rem;
}
</style>