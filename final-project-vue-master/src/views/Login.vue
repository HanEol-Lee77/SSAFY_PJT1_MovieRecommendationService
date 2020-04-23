<template>
  <v-app>
    <v-content id="login">
      <v-container class="fill-height" fluid>
        <v-row align="start" justify="center">
          <v-col cols="12" sm="8" md="4">
            <LoginForm />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import LoginForm from "@/components/LoginForm";

export default {
  name: "login",

  components: {
    LoginForm
  },
  methods: {}
};
</script>
