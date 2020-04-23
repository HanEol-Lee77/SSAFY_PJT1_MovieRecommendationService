<template>
  <v-card class="elevation-12 pa-10" color="black" width="25rem">
    <v-toolbar color="black" dark flat>
      <v-toolbar-title class="font-weight-bold">회원가입</v-toolbar-title>
      <v-spacer />
    </v-toolbar>
    <v-divider color="red"></v-divider>
    <v-card-text>
      <v-form color="white" @submit.prevent="signup(credentials)">
        <v-text-field
          id="username"
          label="이름"
          name="username"
          type="text"
          color="white"
          dark
          clearable
          :rules="[requiredRule]"
          v-model="credentials.username"
        />
        <v-text-field
          id="email"
          label="이메일 주소"
          name="email"
          type="text"
          color="white"
          dark
          clearable
          :rules="[requiredRule, emailRule]"
          v-model="credentials.email"
        />

        <v-text-field
          id="password1"
          label="비밀번호"
          name="password1"
          type="password"
          color="white"
          dark
          clearable
          :rules="[requiredRule]"
          v-model="credentials.password1"
        />
        <v-text-field
          id="password2"
          label="비밀번호 확인"
          name="password2"
          type="password"
          color="white"
          dark
          clearable
          :rules="[requiredRule]"
          v-model="credentials.password2"
        />
        <v-card-actions>
          <v-spacer />
          <v-btn type="submit" color="red black--text" light class="font-weight-bold">가입</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>

    <v-btn :to="{ name: 'login' }" text color="white" class="text-center">지금 로그인하기</v-btn>
  </v-card>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "signup-form",
  data() {
    return {
      credentials: {}
    };
  },
  computed: mapState("user", ["requiredRule", "emailRule"]),
  methods: mapActions("user", ["signup"])
};
</script>

<style></style>
