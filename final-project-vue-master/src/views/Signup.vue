<template>
  <v-app id="signup">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="start" justify="center">
          <v-col cols="12" sm="8" md="4">
            <SignupForm />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import SignupForm from "@/components/SignupForm";

export default {
  name: "signup",

  components: {
    SignupForm
  }
};
</script>
<style>
</style>
