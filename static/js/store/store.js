import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
	state: {
		pessoa: {},
	},
  mutations: {
    change(state, pessoa) {
      state.pessoa = pessoa;
    }
  },
  getters: {
    pessoa: state => state.pessoa
  }
});