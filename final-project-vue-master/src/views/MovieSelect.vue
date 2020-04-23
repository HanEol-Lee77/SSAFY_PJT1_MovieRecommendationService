<template>
  <div class="movie-list">
    <v-container>
      <div style="height: 100px;"></div>
      <v-stepper v-model="e6" vertical>
        <v-stepper-step :complete="e6 > 1" step="1">좋아하는 장르의 영화를 선택해주세요</v-stepper-step>

        <v-stepper-content step="1">
          <v-card color="grey lighten-1" class="mb-12">
            <v-card class="mx-auto">
              <SelectGroup
                v-for="(movies, i) in moviesToSelect.slice(0, 4)"
                :key="i"
                :movies="movies"
                :selected.sync="selectedMovies[i]"
              />
            </v-card>
          </v-card>
          <v-btn color="primary" @click="goNextStep">Continue</v-btn>
        </v-stepper-content>

        <v-stepper-step :complete="e6 > 2" step="2">좋아하는 국가의 영화를 선택해주세요</v-stepper-step>

        <v-stepper-content step="2">
          <v-card color="grey lighten-1" class="mb-12">
            <v-card class="mx-auto">
              <SelectGroup
                v-for="(movies, i) in moviesToSelect.slice(4, 6)"
                :key="i"
                :movies="movies"
                :selected.sync="selectedMovies[i]"
              />
            </v-card>
          </v-card>

          <v-btn color="primary" @click="goNextStep">Continue</v-btn>
          <v-btn text @click="goPreviousStep">Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step :complete="e6 > 3" step="3">좋아하는 관람 등급의 영화를 선택해주세요</v-stepper-step>

        <v-stepper-content step="3">
          <v-card color="grey lighten-1" class="mb-12">
            <v-card class="mx-auto">
              <SelectGroup
                v-for="(movies, i) in moviesToSelect.slice(6, 8)"
                :key="i"
                :movies="movies"
                :selected.sync="selectedMovies[i]"
              />
            </v-card>
          </v-card>
          <v-btn color="primary" @click="goNextStep">Continue</v-btn>
          <v-btn text @click="goPreviousStep">Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="4">View setup instructions</v-stepper-step>
        <v-stepper-content step="4">
          <v-card color="grey lighten-1" class="mb-12">
            <v-card class="mx-auto">
              <SelectGroup
                v-for="(movies, i) in moviesToSelect.slice(8, 10)"
                :key="i"
                :movies="movies"
                :selected.sync="selectedMovies[i]"
              />
            </v-card>
          </v-card>
          <v-btn color="primary" @click="validateAndSetSelectedMovies">Done!</v-btn>
          <v-btn text @click="goPreviousStep">Cancel</v-btn>
        </v-stepper-content>
      </v-stepper>

      <v-row class="my-10" align="center" justify="center">
        <v-btn x-large>취향 분석 시작</v-btn>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import SelectGroup from '@/components/SelectGroup'

export default {
  name: 'movie-select',
  components: {
    SelectGroup
  },
  data() {
    return {
      e6: 1,
      selectedMovies: [],
      fixedSelectedMovies: []
    }
  },
  methods: {
    goNextStep() {
      if (
        this.selectedMovies != [] &&
        this.selectedMovies.every(elem => elem != undefined)
      ) {
        this.fixedSelectedMovies = this.selectedMovies.slice()
        this.e6 = this.e6 + 1
      } else {
        alert('선택하지 않은 영화가 있어요!')
      }
    },
    goPreviousStep() {
      this.selectedMovies = this.fixedSelectedMovies.slice()
      this.e6 = this.e6 - 1
    },
    validateAndSetSelectedMovies() {
      if (this.selectedMovies.every(elem => elem != undefined)) {
        this.setSelectedMovies(this.selectedMovies)
      } else {
        alert('선택하지 않은 영화가 있어요!')
      }
    },
    ...mapActions('movie', ['getMoviesToSelect', 'setSelectedMovies'])
  },
  computed: mapState('movie', ['moviesToSelect']),
  mounted() {
    this.$store.dispatch('user/requireAuth')
    this.getMoviesToSelect()
  }
}
</script>
