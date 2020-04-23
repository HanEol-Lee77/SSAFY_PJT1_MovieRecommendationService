<template>
  <v-card class="mx-auto" background-color="black" max-width="13vw">
    <v-img :src="movie.image" :alt="movie.title" width="13vw"></v-img>

    <v-card-title>{{ movie.title }}</v-card-title>
  </v-card>
</template>

<script>
export default {
  name: "movie-card",
  props: {
    movie: Object
  }
};
</script>

<style>
</style>
