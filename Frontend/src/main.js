import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import Aura from "@primevue/themes/aura";
import Button from "primevue/button";
import Tree from 'primevue/tree';

const app = createApp(App);

app.use(router);

app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            darkModeSelector: 'system'
        }
    },
});

app.component("Button", Button);
app.component("Tree", Tree);

app.mount('#app');

