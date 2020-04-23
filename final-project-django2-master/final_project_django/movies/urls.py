from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.admin_movies, name='admin_movies'),
    path('research/', views.research, name='research'),
    path('recommend/', views.recommend, name='recommed'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/reviews/', views.reviews, name='reviews'),
    path('<int:movie_pk>/reviews/create/', views.create_review, name='create_review'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
    path('<int:movie_pk>/reviews/<int:review_pk>/update/', views.update_review, name='update_review'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),
]