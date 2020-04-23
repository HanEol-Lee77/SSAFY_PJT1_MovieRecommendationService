import MovieService from '@/services/MovieService'

export const namespaced = true

export const state = {
  movieToAdd: {},
  movies: [],
  movieGenres: [
    {
      id: 1
    }
  ],
  moviesToSelect: [],
  selectedMovies: [],
  requiredRule: value => !!value || '필수 입력 사항입니다.'
}

export const mutations = {
  SET_MOVIES(state, movies) {
    state.movies = movies
  },
  DELETE_MOVIE(state, movieId) {
    state.movies = state.movies.filter(movie => movie.id !== movieId)
  },
  SET_MOVIES_TO_SELECT(state, moviesToSelect) {
    state.moviesToSelect = []
    for (let i = 0; i < 12; i = i + 3) {
      state.moviesToSelect.push(moviesToSelect.slice(i, i + 3))
    }
    for (let i = 12; i < 24; i = i + 2) {
      state.moviesToSelect.push(moviesToSelect.slice(i, i + 2))
    }
  },
  SET_SELECTED_MOVIES(state, selectedMovies) {
    state.selectedMovies = selectedMovies
  }
}

export const actions = {
  getMovies({ commit }) {
    MovieService.fetchMovies()
      .then(res => {
        commit('SET_MOVIES', res.data)
      })
      .catch(() => {
        alert('영화 정보를 가져오는데 실패했습니다.')
      })
  },
  createMovie({ dispatch }) {
    MovieService.createMovie()
      .then(() => {
        dispatch('getMovies')
      })
      .catch(() => {
        alert('새 영화 등록에 실패했습니다')
      })
  },
  deleteMovieFromList({ commit }, movieId) {
    MovieService.deleteMovie(movieId)
      .then(() => {
        commit('DELETE_MOVIE', movieId)
      })
      .catch(() => {
        alert('영화 삭제 중 오류가 발생했습니다')
      })
    // dispatch('getUserList')
  },
  getMoviesToSelect({ commit }) {
    MovieService.fetchMoviesToSelect()
      .then(res => {
        commit('SET_MOVIES_TO_SELECT', res.data)
      })
      .catch(() => {
        alert('선택할 영화 정보를 가져오는데 실패했습니다.')
      })
  },
  setSelectedMovies({ commit }, selectedMovies) {
    commit('SET_SELECTED_MOVIES', selectedMovies)
  }
}

export const getters = {}
