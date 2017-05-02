import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'
new Vue({
  el: '#app',
  render: h => h(App)
})
