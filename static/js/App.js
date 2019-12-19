import Vue from 'vue';
import Router from 'vue-router';
import Principal from './components/Principal.vue';
import Inicial from './components/Inicial.vue';
import Pagina2 from './components/Pagina2.vue';
import 'ant-design-vue/dist/antd.css';
import Antd from 'ant-design-vue';
import VueMask from 'v-mask'
import './styles/styles.scss';
import './fonts/fonts.css';
import './fonts/font_sf.css';
import { store } from './store/store'

Vue.use(Router);
Vue.use(Antd);
Vue.use(VueMask);

const routes = [
    { path: '/', name: 'inicial', component: Inicial },
    { path: '/pagina2', name: 'pagina2', component: Pagina2 },
]

const router = new Router({ routes });


new Vue({
    el: '#main',
    router,
    store,
    template: '<Principal />',
    components: { Principal },
});