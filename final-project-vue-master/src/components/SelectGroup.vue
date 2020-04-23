<template>
  <v-item-group v-model="clicked" @change="emitOnClick">
    <v-row>
      <v-col v-for="(movie, i) in movies" :key="i" cols="12" md="4">
        <v-item v-slot:default="{ active, toggle }">
          <v-img :src="movie.image" class="text-right pa-2" @click="toggle">
            <v-btn icon dark>
              <v-icon>{{ active ? 'mdi-heart' : 'mdi-heart-outline' }}</v-icon>
            </v-btn>
          </v-img>
        </v-item>
      </v-col>
    </v-row>
  </v-item-group>
</template>

<script>
export default {
  name: 'select-group',
  data() {
    return {
      clicked: undefined
    }
  },
  props: {
    movies: Array
  },

  methods: {
    emitOnClick() {
      this.$emit('update:selected', this.clicked)
    }
  }
}
</script>

<style>
</style>