import { createRouter, createWebHistory } from 'vue-router'
import ItemsList from '@/components/ItemsList.vue'
import ItemData from '@/components/ItemData.vue'
import GetItems from "@/components/GetItems.vue";
import CreateItem from "@/components/CreateItem.vue";
// import App from "@/App.vue";

const routes = [
    { path: '/', component: GetItems },
    { path: '/create-item', component: CreateItem, props: true }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router