<template>
  <v-app app id="admin-user-list">
    <AdminUsers />
  </v-app>
</template>

<script>
import AdminUsers from '@/components/AdminUsers'

export default {
  name: 'admin-user-list',
  components: {
    AdminUsers
  },
  mounted() {
    this.$store.dispatch('user/requireAuth')
  }
}
</script>
