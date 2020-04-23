<template>
  <div>
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on }">
        <v-btn text outlined color="primary" dark v-on="on">등록</v-btn>
      </template>

      <v-card>
        <v-card-title class="headline black d-flex justify-space-between" primary-title>
          새 영화
          <v-btn color="black" @click="dialog = false">
            <v-icon color="white">mdi-close</v-icon>
          </v-btn>
        </v-card-title>

        <v-card-text>
          <v-form color="white" @submit.prevent="createMovie(movieToAdd)">
            <v-text-field
              id="title"
              label="영화 제목"
              name="title"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.title"
            />

            <v-textarea
              id="summary"
              label="줄거리"
              name="summary"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.summary"
            />
            <v-text-field
              id="directorNm"
              label="감독 이름"
              name="directorNm"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.directorNm"
            />
            <div id="example-3">
              <input type="checkbox" id="1" value="2" v-model="checkedNames" />
              <label for="1">로맨스</label>
              <input type="checkbox" id="2" value="2" v-model="checkedNames" />
              <label for="2">판타지</label>
              <input type="checkbox" id="3" value="3" v-model="checkedNames" />
              <label for="3">미스터리</label>
              <br />
              <span>체크한 이름: {{ checkedNames }}</span>
            </div>
            <v-text-field
              id="genresCds"
              label="장르"
              name="genresCds"
              type="text"
              color="white"
              hint="'|'를 이용하여 여러 배우명을 입력해주세요"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.genresNm"
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
              :rules="[requiredRule]"
              v-model="movieToAdd.prdtYear"
            />
            <v-text-field
              id="openDt"
              label="개봉일자"
              name="openDt"
              type="number"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.openDt"
            />
            <v-text-field
              id="showTm"
              label="러님타임(분)"
              name="showTm"
              type="number"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.showTm"
            />
            <v-text-field
              id="nationNm"
              label="제작국가"
              name="nationNm"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.nationNm"
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
              :rules="[requiredRule]"
              v-model="movieToAdd.actorsNm"
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
              :rules="[requiredRule]"
              v-model="movieToAdd.watchGradeNm"
            />
            <v-text-field
              id="companyNmDict"
              label="제작사"
              name="companyNmDict"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.companyNmDict"
            />
            <v-text-field
              id="link"
              label="영화 정보 URL"
              name="link"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.link"
            />
            <v-text-field
              id="image"
              label="영화 포스터 URL"
              name="image"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.image"
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
              :rules="[requiredRule]"
              v-model="movieToAdd.userRating"
            />
            <v-text-field
              id="audiAcc"
              label="관객수"
              name="audiAcc"
              type="text"
              color="white"
              dark
              clearable
              :rules="[requiredRule]"
              v-model="movieToAdd.audiAcc"
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
              :rules="[requiredRule]"
              v-model="movieToAdd.thumbsNm"
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
              :rules="[requiredRule]"
              v-model="movieToAdd.thumbsImage"
              @keyup.enter="createMovie"
            />
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" type="submit" text outlined>등록</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'movie-create-form-modal',
  data() {
    return {
      dialog: false
    }
  },
  computed: mapState('movie', ['movieToAdd', 'requiredRule']),
  methods: mapActions('movie', ['createMovie'])
}
</script>

<style>
</style>
