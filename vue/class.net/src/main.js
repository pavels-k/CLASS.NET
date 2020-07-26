import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import vuetify from './plugins/vuetify';
import {D3BarChart} from 'vue-d3-charts'

Vue.use(Vuetify)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  D3BarChart,
  render: h => h(App)
}).$mount('#app')
