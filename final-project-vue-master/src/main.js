import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'
import vuetify from './plugins/vuetify';
import VAnimateCss from 'v-animate-css';
import store from './store'

Vue.config.productionTip = false
Vue.use(VueSession)
Vue.use(VAnimateCss);

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')