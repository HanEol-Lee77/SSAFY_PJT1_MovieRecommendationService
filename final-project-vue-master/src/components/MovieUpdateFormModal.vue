<template>
  <div>
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on }">
        <v-btn text outlined color="success" dark v-on="on">수정</v-btn>
      </template>

      <v-card>
        <v-card-title class="headline black d-flex justify-space-between" primary-title>
          영화 정보 수정
          <v-btn color="black" @click="dialog = false">
            <v-icon color="white">mdi-close</v-icon>
          </v-btn>
        </v-card-title>

        <v-card-text>
          <v-form color="white">
            <v-text-field
              id="title"
              label="영화 제목"
              name="title"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.title"
            />

            <v-textarea
              id="summary"
              label="줄거리"
              name="summary"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.summary"
            />
            <v-text-field
              id="directorNm"
              label="감독 이름"
              name="directorNm"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.directorNm"
            />
            <v-text-field
              id="genresNm"
              label="장르"
              name="genresNm"
              type="text"
              color="white"
              hint="'|'를 이용하여 여러 배우명을 입력해주세요"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.genresNm"
            />
            <!-- <v-row align="center">
              <v-col class="d-flex" v-model="movie.genreNm" cols="12" sm="6">
                <v-select :items="genres" label="장르"></v-select>
              </v-col>
            </v-row>-->
            <v-text-field
              id="prdtYear"
              label="제작연도"
              name="prdtYear"
              type="number"
              color="white"
              min="1900"
              max="2019"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.prdtYear"
            />
            <v-text-field
              id="openDt"
              label="개봉일자"
              name="openDt"
              type="number"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.openDt"
            />
            <v-text-field
              id="showTm"
              label="러님타임(분)"
              name="showTm"
              type="number"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.showTm"
            />
            <v-text-field
              id="nationNm"
              label="제작국가"
              name="nationNm"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.nationNm"
            />
            <v-text-field
              id="actorsNm"
              label="배우명"
              name="actorsNm"
              type="text"
              color="white"
              hint="'|'를 이용하여 여러 배우명을 입력해주세요 예시) 유해진|조진웅|이서진|염정아|김지수"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.actorsNm"
            />
            <v-text-field
              id="watchGradeNm"
              label="관람등급"
              name="watchGradeNm"
              type="text"
              color="white"
              hint="예시) 12세이상관람가"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.watchGradeNm"
            />
            <v-text-field
              id="companyNmDict"
              label="제작사"
              name="companyNmDict"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.companyNmDict"
            />
            <v-text-field
              id="link"
              label="영화 정보 URL"
              name="link"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.link"
            />
            <v-text-field
              id="image"
              label="영화 포스터 URL"
              name="image"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.image"
            />
            <v-text-field
              id="userRating"
              label="유저 평점"
              name="userRating"
              type="text"
              color="white"
              hint="예시) 7.88"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.userRating"
            />
            <v-text-field
              id="audiAcc"
              label="관객수"
              name="audiAcc"
              type="text"
              color="white"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.audiAcc"
            />
            <v-text-field
              id="thumbsNm"
              label="함꼐 보면 좋은 영화"
              name="thumbsNm"
              type="text"
              color="white"
              hint="'|'를 이용하여 여러 영화명을 입력해주세요 예시) 로켓맨|싱 스트리트|위대한 쇼맨|라라랜드|브로드웨이 4D"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.thumbsNm"
            />
            <v-text-field
              id="thumbsImage"
              label="함꼐 보면 좋은 영화 포스터 URL"
              name="thumbsImage"
              type="text"
              color="white"
              hint="'|'를 이용하여 여러 URL을 입력해주세요"
              dark
              clearable
              :rules="[rules.required]"
              v-model="movie.thumbsImage"
              @keyup.enter="createMovie"
            />
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" text outlined @click="updateMovie">수정</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
  name: "MovieUpdateFormModal",
  data() {
    return {
      dialog: false,
      movie: {},
      rules: {
        required: value => !!value || "필수 입력 사항입니다."
      }
    };
  },
  props: {
    movieId: Number
  },
  methods: {
    getPrevMovie() {
      const token = this.$session.get("jwt");
      const options = {
        headers: { Authorization: `JWT ${token}` }
      };
      axios
        .get(`http://localhost:8000/api/v1/movies/${this.movieId}/`, options)
        .then(res => (this.movie = res.data));
    },
    updateMovie(e) {
      const movieId = e.target.parentNode.getAttribute("value-id");
      const token = this.$session.get("jwt");
      const options = {
        headers: { Authorization: `JWT ${token}` }
      };
      axios
        .post(
          `http://localhost:8000/api/v1/movies/${this.movieId}/update/`,
          this.movie,
          options
        )
        .then(res =>
          router.push(`/admin-movie-list?${Date.now()}`).catch(err => {})
        );
    }
  },
  mounted() {
    this.getPrevMovie();
  }
};
</script>

<style></style>
