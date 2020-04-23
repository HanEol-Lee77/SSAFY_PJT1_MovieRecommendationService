from django.shortcuts import render, get_object_or_404
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Movie, Review
import random

# Create your views here.

def home(request):
    pass

@api_view(['GET'])
def admin_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def research(request):
#     movies = Movie.objects.all()
#     research_movies = []
#     while len(research_movies) < 15:
#         num = random.randrange(1, 199)
#         if num not in research_movies:
#             research_movies.append(num)
#     queryset = Movie.objects.filter(pk__in=research_movies)
#     serializer = MovieSerializer(queryset, many=True)
#     return Response(serializer.data)]

@api_view(['GET'])
def research(request):
    research_movies = []

    pk_group1 = [1, 2, 5, 21, 23]
    pk_group2 = [3, 6, 10, 14, 20]
    pk_group3 = [4, 7, 9, 13, 18, 22, 25]
    pk_group4 = [8, 16, 19]
    pk_group5 = [11, 12, 24, 28]
    pk_group6 = [15, 17, 26, 27]
    movie_group1 = Movie.objects.filter(genresCds__in=pk_group1)
    movie_group2 = Movie.objects.filter(genresCds__in=pk_group2)
    movie_group3 = Movie.objects.filter(genresCds__in=pk_group3)
    movie_group4 = Movie.objects.filter(genresCds__in=pk_group4)
    movie_group5 = Movie.objects.filter(genresCds__in=pk_group5)
    movie_group6 = Movie.objects.filter(genresCds__in=pk_group6)
    movie_group = [0, movie_group1, movie_group2, movie_group3, movie_group4, movie_group5, movie_group6]
    ordering = [1, 3, 5, 1, 4, 6, 2, 3, 6, 2, 5, 4]
    for i in ordering:
        while True:
            random_num = random.randrange(0, len(movie_group[i]))
            if movie_group[i][random_num].pk not in research_movies:
                research_movies.append(Movie.objects.get(pk=movie_group[i][random_num].pk))
                break

    movie_group1 = Movie.objects.filter(nationNm="한국")
    movie_group2 = Movie.objects.exclude(nationNm="한국")
    movie_group = [0, movie_group1, movie_group2]
    ordering = [1, 2, 1, 2]
    for i in ordering:
        while True:
            random_num = random.randrange(0, len(movie_group[i]))
            if movie_group[i][random_num].pk not in research_movies:
                research_movies.append(Movie.objects.get(pk=movie_group[i][random_num].pk))
                break

    movie_group1 = Movie.objects.filter(watchGradeNm="전체관람가")
    movie_group2 = Movie.objects.filter(watchGradeNm="12세관람가")
    movie_group3 = Movie.objects.filter(watchGradeNm="15세관람가")
    movie_group4 = Movie.objects.filter(watchGradeNm="18세관람가")
    movie_group = [0, movie_group1, movie_group2, movie_group3, movie_group4]
    ordering = [1, 4, 2, 3]
    for i in ordering:
        while True:
            random_num = random.randrange(0, len(movie_group[i]))
            if movie_group[i][random_num].pk not in research_movies:
                research_movies.append(Movie.objects.get(pk=movie_group[i][random_num].pk))
                break
    
    movie_group1 = Movie.objects.filter(showTm__lt = 90)
    movie_group2 = Movie.objects.filter(showTm__range = (90, 120))
    movie_group3 = Movie.objects.filter(showTm__range = (121, 150))
    movie_group4 = Movie.objects.filter(showTm__gt = 150)
    movie_group = [0, movie_group1, movie_group2, movie_group3, movie_group4]
    ordering = [1, 4, 2, 3]
    for i in ordering:
        while True:
            random_num = random.randrange(0, len(movie_group[i]))
            if movie_group[i][random_num].pk not in research_movies:
                research_movies.append(Movie.objects.get(pk=movie_group[i][random_num].pk))
                break

    # queryset = Movie.objects.filter(pk__in=research_movies)
    serializer = MovieSerializer(research_movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def recommend(request):
    pass
#     num = 1
#     for i in request.data:
#         if num <= 12:
            
#         elif num <= 16:
        
#         elif num <= 20:

#         else:
        
#         num += 1
        

# @api_view(['POST'])
# def recommend(request):
#     movies = Movie.objects.all()
#     movie_scores = []
#     movie_ids = []
#     recommended_movies = []
#     for movie in movies:
#         temp_score = 0
#         genre_list = movie.genresNm.split('|')
#         actor_list = movie.actorsNm.split('|')
#         for movie_data in request.data:
#             if movie.directorNm == movie_data.directorNm:
#                 temp_score += 1
#             movie_data_genre_list = movie_data.genresNm.split('|')
#             for movie_genre in genre_list:
#                 for movie_data_genre in movie_data_genre_list:
#                     if movie_genre == movie_data_genre:
#                         temp_score += 1
#                         break
#             if movie_data.showTm-30 <= movie.showTm <= movie_data.showTm+30:
#                 temp_score += 1
#             if movie.nationNm == "한국":
#                 if movie_data.nationNm == "한국":
#                     temp_score += 1
#             else:
#                 if movie_data.nationNm != "한국":
#                     temp_score += 1
#             if movie.watchGradeNm == movie_data.watchGradeNm:
#                 temp_score += 1
#             movie_data_actor_list = movie_data.actorsNm.split('|')
#             for movie_actor in actor_list:
#                 for movie_data_actor in movie_data_actor_list:
#                     if movie_actor == movie_data_actor:
#                         temp_score += 1
#                         break
#         if float(movie.userRating) > 8:
#             temp_score += 1
#         if int(movie.audiAcc) > 50000000:
#             temp_score += 1
#         movie_scores.append(temp_score)
#     pivot_score = (max(movie_scores) + min(movie_scores)) // 2
#     for idx in range(0, len(movie_scores)):
#         if pivot_score < movie_scores[idx]:
#             movie_ids.append(idx+1)
#     while len(recommended_movies) < 5:
#         num = random.randrange(1, len(movie_scores)+1)
#         if num in movie_ids:
#             if num not in recommended_movies:
#                 recommended_movies.append(num)
#     queryset = Movie.objects.filter(pk__in=recommended_movies)
#     serializer = MovieSerializer(queryset, many=True)
#     return Response(serializer.data)



@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request, movie_pk):
    # review = Review(request.data)
    # review.score = 1
    # review.user = request.user
    # review.movie_id = movie_pk
    # review.save()
    # return Response({message: "리뷰가 생성되었습니다."})
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie_id=movie_pk)
    # return Response(serializer.data)
    return Response(status=200)

@api_view(['GET'])
def reviews(request, movie_pk):
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    # return Response(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def delete_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    # return Response(serializer.data)
    return Response(status=200)

@api_view(['POST'])
def update_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(data=request.data, instance=review)
    if serializer.is_valid():
        serializer.save()
    return Response(status=200)

@api_view(['POST'])
def create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(status=200)

@api_view(['POST'])
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return Response(status=200)

@api_view(['POST'])
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(data=request.data, instance=movie)
    if serializer.is_valid():
        serializer.save()
    return Response(status=200)
