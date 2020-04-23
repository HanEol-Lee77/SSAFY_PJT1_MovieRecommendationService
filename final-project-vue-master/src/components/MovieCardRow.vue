<template>
  <v-row class="d-flex">
    <v-col v-for="movie in movies" :key="movie.id">
      <MovieCard
        v-animate-css.hover="'pulse'"
        v-animate-css.click="'rubberBand'"
        :movie="movie"
        @click.native="select(movie)"
      />
    </v-col>
  </v-row>
</template>

<script>
import MovieCard from "@/components/MovieCard";

export default {
  name: "MovieCardRow",
  components: {
    MovieCard
  },
  data() {
    return {};
  },
  props: {
    movies: Array
  },
  methods: {
    select(movie) {
      this.$emit("selected", movie);
    }
  }
};
</script>

<style>
.selected {
  background-color: rgba(0, 0, 0, 0.5);
}
</style>
