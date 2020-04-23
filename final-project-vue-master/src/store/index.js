import Vue from 'vue'
import Vuex from 'vuex'
import * as user from '@/store/modules/user'
import * as movie from '@/store/modules/movie'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    a: 1
  },
  mutations: {},
  actions: {},
  modules: {
    user,
    movie
  }
})
