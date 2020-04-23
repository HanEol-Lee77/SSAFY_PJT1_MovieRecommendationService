import axios from 'axios'
import * as user from '@/store/modules/user.js'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: false
  // headers: {
  //   Accept: "application//json",
  //   "Content-Type": "application/json"
  // }
})

const setOptions = () => {
  const token = user.state.token
  return {
    headers: { Authorization: `JWT ${token}` }
  }
}

export default {
  createUser(credentials) {
    return apiClient.post('/api/v1/accounts/signup/', credentials)
  },
  loginUser(credentials) {
    return apiClient.post('/api-token-auth/', credentials)
  },
  fetchUser(userId) {
    return apiClient.get(`/api/v1/accounts/${userId}/`, setOptions())
  },
  fetchUsers() {
    return apiClient.get(`/api/v1/accounts/admin/`, setOptions())
  },
  deleteUser(userId) {
    return apiClient.post(
      `/api/v1/accounts/${userId}/delete/`,
      {},
      setOptions()
    )
  }
}
