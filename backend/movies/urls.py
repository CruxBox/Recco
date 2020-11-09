from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('search/<str:query>/<int:max_results>', search_movies, name='search_movies'),
    path('popular/<int:max_results>', get_popular_movies, name='popular_movies'),
    path('latest/', get_latest_movies, name='latest_movie'),
    path('top-rated/<int:max_results>', get_top_rated, name='top_rated_movies'),
    path('upcoming/<int:max_results>', get_upcoming, name='upcoming_movies')
]