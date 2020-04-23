<template>
  <v-card class="elevation-12 pa-10" color="black" width="25rem">
    <v-toolbar color="black" dark flat>
      <v-toolbar-title class="font-weight-bold">로그인</v-toolbar-title>
      <v-spacer />
    </v-toolbar>

    <v-divider color="red"></v-divider>
    <v-card-text>
      <v-form color="white" @submit.prevent="login(credentials)">
        <v-text-field
          id="username"
          label="사용자 이름"
          name="username"
          type="text"
          color="white"
          dark
          clearable
          :rules="[requiredRule]"
          v-model="credentials.username"
        />

        <v-text-field
          id="password"
          label="비밀번호"
          name="password"
          type="password"
          color="white"
          dark
          clearable
          :rules="[requiredRule]"
          v-model="credentials.password"
          @keyup.enter="login"
        />
        <v-card-actions>
          <v-spacer />
          <v-btn color="red black--text" light class="font-weight-bold" type="submit">로그인</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>

    <v-btn :to="{ name: 'signup' }" text color="white">혹시 아직 회원이 아니신가요?</v-btn>
  </v-card>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "login-form",
  data() {
    return {
      credentials: {}
    };
  },
  computed: mapState("user", ["requiredRule"]),
  methods: mapActions("user", ["login"])
};
</script>

<style></style>
