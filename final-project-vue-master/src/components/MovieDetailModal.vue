<template>
    <div>
        <v-dialog
            v-model="dialog"
            @input="v => v || modalOn()"
            width="50vw"
            persistent
        >
            <template v-slot:activator="{ on }">
                <v-btn outlined dark v-on="on" @click="modalOn"
                    >상세 보기</v-btn
                >
            </template>

            <v-card style="width: 48vw;">
                <v-card-title
                    class="headline black d-flex justify-space-between"
                    primary-title
                >
                    영화 상세 정보
                    <v-btn color="black" @click="modalOn">
                        <v-icon color="white">mdi-close</v-icon>
                    </v-btn>
                </v-card-title>
                <v-row justify="space-around" align="center">
                    <v-col justify="space-around" align="center">
                        <v-img
                            :src="movie.image"
                            :alt="movie.title"
                            width="17vw"
                        ></v-img>
                    </v-col>
                    <v-col>
                        <v-card-text>
                            <h2 class="font-weight-bold title primary--text">
                                {{ movie.title }}
                            </h2>
                            <br />
                            <p>{{ movie.genresNm.split("|").join(", ") }}</p>
                            <p>{{ movie.actorsNm.split("|").join(", ") }}</p>
                            <p>{{ movie.summary }}</p>
                        </v-card-text>
                    </v-col>
                </v-row>

                <v-divider></v-divider>
                <v-container>
                    <v-form color="white">
                        <v-row justify="center" align="center">
                            <v-col cols="12" md="4">
                                <v-text-field
                                    id="comment"
                                    label="댓글"
                                    name="comment"
                                    type="text"
                                    color="white"
                                    dark
                                    clearable
                                    :counter="50"
                                    required
                                    outlined
                                    v-model="review.comment"
                                />
                            </v-col>
                            <v-col cols="6" md="2">
                                <v-text-field
                                    id="score"
                                    label="평점"
                                    name="score"
                                    type="number"
                                    color="white"
                                    min="1"
                                    max="10"
                                    dark
                                    required
                                    outlined
                                    v-model="review.score"
                                />
                            </v-col>
                            <v-col cols="6" md="2">
                                <v-btn @click="createReview">평점 남기기</v-btn>
                            </v-col>
                        </v-row>
                    </v-form>
                    <v-row
                        v-for="rev in reviews"
                        :key="rev.id"
                        justify="center"
                        align="center"
                    >
                        <v-col justify="center" align="center">{{
                            rev.comment
                        }}</v-col>
                        <v-col justify="center" align="center">{{
                            rev.score
                        }}</v-col>
                        <v-col justify="start" align="center"
                            ><v-btn
                                @click="deleteReview"
                                :value="rev.id"
                                color="error"
                                >삭제</v-btn
                            ></v-col
                        >
                    </v-row>
                </v-container>
                <v-row>
                    <!-- <v-col v-for="idx of movie.thumsNm">
                        <v-img></v-img> -->
                    <!-- </v-col> -->
                </v-row>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import axios from "axios";
import JwtDecode from "jwt-decode";

export default {
    name: "MovieDetailModal",
    data() {
        return {
            dialog: false,
            review: {},
            reviews: []
        };
    },
    props: {
        movie: Object
    },
    methods: {
        modalOn() {
            this.$emit("modalOn");
            this.dialog = false;
        },
        createReview() {
            const token = this.$session.get("jwt");
            const options = {
                headers: { Authorization: `JWT ${token}` }
            };
            this.review.user = JwtDecode(token).user_id;
            this.review.movie = this.movie;
            axios
                .post(
                    `http://localhost:8000/api/v1/movies/${this.movie.id}/reviews/create/`,
                    this.review,
                    options
                )
                .then(res => this.getReviews());
        },
        getReviews() {
            const token = this.$session.get("jwt");
            const options = {
                headers: { Authorization: `JWT ${token}` }
            };
            axios
                .get(
                    `http://localhost:8000/api/v1/movies/${this.movie.id}/reviews/`,
                    options
                )
                .then(res => (this.reviews = res.data));
        },
        deleteReview(e) {
            const token = this.$session.get("jwt");
            const options = {
                headers: { Authorization: `JWT ${token}` }
            };
            this.review.user = JwtDecode(token).user_id;
            this.review.movie = this.movie;
            axios
                .post(
                    `http://localhost:8000/api/v1/movies/${
                        this.movie.id
                    }/reviews/${e.target.closest("button").value}/delete/`,
                    {},
                    options
                )
                .then(res => this.getReviews());
        }
    },
    mounted() {
        this.getReviews();
    }
};
</script>

<style></style>
