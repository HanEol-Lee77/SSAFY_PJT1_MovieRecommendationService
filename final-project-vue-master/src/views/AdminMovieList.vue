<template>
  <v-app id="admin-movie-list">
    <AdminMovies />
  </v-app>
</template>

<script>
import AdminMovies from '@/components/AdminMovies'

export default {
  name: 'admin-movie-list',
  components: {
    AdminMovies
  },
  data() {
    return {
      dialog: false
    }
  },
  mounted() {
    this.$store.dispatch('user/requireAuth')
  }
}
</script>
