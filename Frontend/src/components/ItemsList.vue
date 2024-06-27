<script setup>
import {ref, reactive, onMounted} from "vue";
import axios from 'axios';
import ProgressSpinner from 'primevue/progressspinner';


const nodes = ref([
  {
    key: "1",
    label: "Node 1",
    children: [
      {
        key: "1.1",
        label: "Child Node 1.1",
        children: []
      },
      {
        key: "1.2",
        label: "Child Node 1.2",
        children: []
      }
    ]
  },
  {
    key: "2",
    label: "Node 2",
    children: []
  }
]);

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
  Object.keys(expandedKeys).forEach(key => {
    delete expandedKeys[key];
  });
};

const onNodeSelect = (node) => {
  console.log('Выбран узел:', node);
};

const nodes_ = ref(null);

const fetchItems = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/items/');
    nodes_.value = response.data;
  } catch (e) {
    console.error(e);
  }
};
onMounted(fetchItems);
</script>

<template>
  <div class="flex flex-wrap gap-2 mb-6">
    <Button type="button" icon="pi pi-plus" label="Expand All" @click="expandAll" class="button-expand"/>
    <Button type="button" icon="pi pi-minus" label="Collapse All" @click="collapseAll"/>
  </div>

  <div v-if="nodes_">
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