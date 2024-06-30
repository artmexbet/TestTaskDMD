<script setup>
import {ref, reactive, onMounted} from "vue";
import axios from 'axios';
import ProgressSpinner from 'primevue/progressspinner';
import Button from "primevue/button";
import Tree from 'primevue/tree';
import {serverUrl} from "@/config.js";

// Создаем объект expandedKeys
const expandedKeys = reactive({});
const selectedKeys = ref([]);

// Функция для добавления всех ключей в expandedKeys
const addAllKeys = (nodes) => {
  nodes.forEach(node => {
    expandedKeys[node.key] = true;
    if (node.children) {
      addAllKeys(node.children);
    }
  });
};

// Функция для разворачивания всех узлов
const expandAll = () => {
  addAllKeys(nodes.value);
};

// Функция для схлопывания всех узлов
const collapseAll = () => {
  for (let key in expandedKeys) {
    delete expandedKeys[key];
  }
};

const emit = defineEmits(['selected-item']);

const onNodeSelect = (node) => {
  console.log('Выбран узел:', node);
  emit('selected-item', node);
};

const nodes = ref(null);

const fetchItems = async () => {
  try {
    const response = await axios.get(`${serverUrl}/tasks/`);
    nodes.value = response.data;
  } catch (e) {
    console.error(e);
  }
};
onMounted(fetchItems);
</script>

<template>
  <div class="flex flex-wrap gap-2 mb-6">
    <Button type="button" label="Развернуть все" @click="expandAll" class="button-expand"/>
    <Button type="button" label="Свернуть все" @click="collapseAll"/>
  </div>

  <div v-if="nodes">
    <Tree v-model:selection-keys="selectedKeys" v-model:expandedKeys="expandedKeys"
          selection-mode="single" :value="nodes" class="w-full md:w-[30rem]"
          @node-select="onNodeSelect"></Tree>
  </div>
  <div v-else>
    <ProgressSpinner/>
  </div>
</template>

<style scoped>
.button-expand {
  margin-right: 10px;
}
</style>