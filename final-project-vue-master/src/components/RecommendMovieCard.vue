<template>
    <v-hover ref="myhover">
        <template v-slot:default="{ hover }">
            <v-card class="mx-auto" background-color="black" max-width="13vw">
                <v-img
                    :src="movie.image"
                    :alt="movie.title"
                    width="13vw"
                ></v-img>

                <v-card-title>{{ movie.title }}</v-card-title>
                <v-fade-transition>
                    <v-overlay v-if="hover" absolute color="#036358">
                        <MovieDetailModal :movie="movie" @modalOn="modalOn" />
                    </v-overlay>
                </v-fade-transition>
            </v-card>
        </template>
    </v-hover>
</template>

<script>
import MovieDetailModal from "@/components/MovieDetailModal";

export default {
    name: "RecommendMovieCard",
    components: {
        MovieDetailModal
    },
    data() {
        return {
            props: {
                disabled: false
            }
        };
    },
    props: {
        movie: Object
    },
    methods: {
        modalOn() {
            this.$refs.myhover.disabled = !this.$refs.myhover.disabled;
        }
    }
};
</script>

<style></style>
