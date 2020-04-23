import axios from 'axios'
import * as user from '@/store/modules/user.js'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  // baseURL: 'http://localhost:3000',
  withCredentials: false
})

const setOptions = () => {
  const token = user.state.token
  return {
    headers: { Authorization: `JWT ${token}` }
  }
}

export default {
  fetchMovies() {
    return apiClient.get('/api/v1/movies/', setOptions())
    // return apiClient.get('/movies/')
  },
  createMovie() {
    return apiClient.post(`/api/v1/movies/create/`, {}, setOptions())
    // return apiClient.post(`/movies/`)
  },
  deleteMovie(movieId) {
    return apiClient.post(`/api/v1/movies/${movieId}/delete/`, {}, setOptions())
    // return apiClient.delete(`/movies/${movieId}`)
  },
  fetchMoviesToSelect() {
    return apiClient.get('/api/v1/movies/research/', setOptions())
    // return apiClient.get('/movies/')
  }
}
