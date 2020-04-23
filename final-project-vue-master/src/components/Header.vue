<template>
  <header>
    <v-app-bar app clipped-right color="transparent" dense>
      <v-toolbar-title class="align-center">
        <v-btn to="/" color="transparent">
          <v-icon class="mx-4">mdi-movie</v-icon>
          <span class="title">세 얼간이의 추천 영화</span>
        </v-btn>
      </v-toolbar-title>
      <v-spacer />
      <template v-if="user.is_staff">
        <v-btn text color="white" :to="{ name: 'admin-movie-list'}">영화 관리</v-btn>
        <v-btn text color="white" to="/admin-user-list">유저 관리</v-btn>
      </template>

      <template v-if="user.isLoggedIn">
        <v-btn text color="white" to="/movie-select">내 취향 분석</v-btn>
        <v-btn text color="white" to="/movie-list">추천 영화 보기</v-btn>
        <v-btn text color="white" :to="{ name: 'login' }" v-if="!user.isLoggedIn">로그인</v-btn>
        <v-btn text color="white" @click="logout" v-if="user.isLoggedIn">로그아웃</v-btn>
        <v-btn @click="toggleDrawer">
          <i class="fas fa-user"></i>
        </v-btn>
      </template>
    </v-app-bar>
  </header>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Header',
  computed: mapState('user', ['user']),
  methods: {
    toggleDrawer() {
      this.$emit('toggleDrawer')
    },
    ...mapActions('user', ['logout'])
  }
}
</script>

<style></style>
