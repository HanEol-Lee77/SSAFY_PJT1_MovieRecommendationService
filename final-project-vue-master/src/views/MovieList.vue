<template>
    <v-container>
        <div style="height: 100px;"></div>
        <v-row class="flex-wrap">
            <RecommendMovieCard
                v-for="movie in recommendMovies"
                :key="movie.id"
                :movie="movie"
            />
        </v-row>
    </v-container>
</template>

<script>
import axios from "axios";

import RecommendMovieCard from "@/components/RecommendMovieCard";

export default {
    name: "MovieList",
    components: {
        RecommendMovieCard
    },
    data() {
        return {
            recommendMovies: []
        };
    },
    props: {
        selectedMovies: Array
    },
    methods: {
        recommend() {
            const token = this.$session.get("jwt");
            const options = {
                headers: { Authorization: `JWT ${token}` }
            };
            axios
                .post(
                    `http://localhost:8000/api/v1/movies/recommend/`,
                    this.selectedMovies,
                    options
                )
                .then(res => (this.recommendMovies = res.data));
        }
    },
    mounted() {
        this.$emit("loggedIn");
        this.recommend();
    }
};
</script>

<style></style>
