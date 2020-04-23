<template>
  <v-row class="home" justify="center" align="center">
    <div class="mx-auto my-auto">
      <h1>지금 바로 취향 분석에 도전하세요 &#127909;&#9193;</h1>
    </div>
  </v-row>
</template>

<script>
import { mapState } from "vuex";
import router from "@/router";

export default {
  name: "home",
  computed: mapState("user", {
    loggedIn: user => user.isLoggedIn
  }),
  mounted() {
    this.$store.dispatch("user/requireAuth");
  }
};
</script>
