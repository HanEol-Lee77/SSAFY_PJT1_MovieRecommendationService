import router from '@/router'
import JwtDecode from 'jwt-decode'
import UserService from '@/services/UserService'

export const namespaced = true

export const state = {
  user: {},
  token: '',
  users: {},
  requiredRule: value => !!value || '필수 입력 사항입니다.',
  emailRule: value => {
    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    return pattern.test(value) || '이메일 주소를 입력해주세요'
  }
}

export const mutations = {
  SET_TOKEN(state, token) {
    state.token = token
  },
  SET_USER(state, user) {
    state.user = user
  },
  SET_USERS(state, users) {
    state.users = users
  },
  UNSET_USER(state) {
    state.user = {}
  },
  DELETE_USER(state, userId) {
    state.users = state.users.filter(user => user.id !== userId)
  }
}

export const actions = {
  signup({ dispatch }, credentials) {
    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    if (!credentials.email) {
      alert('이메일 주소를 입력해주세요')
    } else if (!credentials.password1) {
      alert('비밀번호를 입력해주세요')
    } else if (!credentials.password2) {
      alert('비밀번호 확인을 입력해주세요')
    } else if (!credentials.username) {
      alert('사용자 이름를 입력해주세요')
    } else if (!pattern.test(credentials.email)) {
      alert('올바른 이메일 주소를 입력해주세요')
    } else if (credentials.password1 !== credentials.password2) {
      alert('비밀번호가 서로 다릅니다.')
    } else {
      UserService.createUser(credentials).then(res => {
        //   this.$session.start();
        //   this.$session.set("jwt", res.data.token);
        credentials = {
          username: credentials.username,
          password: credentials.password1
        }
        dispatch('login', credentials)
      })
    }
  },
  login({ commit }, credentials) {
    if (!credentials.username) {
      alert('사용자 이름을 입력해주세요')
    } else if (!credentials.password) {
      alert('비밀번호를 입력해주세요')
    } else {
      UserService.loginUser(credentials)
        .then(res => {
          //   this.$session.start();
          //   this.$session.set("jwt", res.data.token);
          commit('SET_TOKEN', res.data.token)

          const userId = JwtDecode(res.data.token).user_id
          UserService.fetchUser(userId).then(res => {
            res.data.isLoggedIn = true
            commit('SET_USER', res.data)
            //   this.$session.set("username", res.data.username);
            //   this.$session.set("is_staff", res.data.is_staff);
            //   this.$session.set("isLogin", true);
            router.push('/').catch(() => {})
          })
        })
        .catch(err => {
          console.log(err)
          alert('사용자 이름과 패스워드를 다시 한번 확인해주세요')
        })
    }
  },
  logout({ commit }) {
    commit('UNSET_USER')
    router.push('/login')
  },
  getUserList({ commit }) {
    UserService.fetchUsers().then(res => {
      commit('SET_USERS', res.data)
    })
  },
  deleteUserFromList({ commit }, userId) {
    UserService.deleteUser(userId)
      .then(() => {
        commit('DELETE_USER', userId)
      })
      .catch(() => {
        alert('유저 삭제 중 오류가 발생했습니다')
      })
    // dispatch('getUserList')
  },
  requireAuth({ state }) {
    if (!state.user.isLoggedIn) {
      router.push('/login')
    }
  }
}

export const getters = {}
