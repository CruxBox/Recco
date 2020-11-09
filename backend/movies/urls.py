from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('search/', search_movies, name='search_movies'),
    path('popular/', get_popular_movies, name='popular_movies'),
    path('latest/', get_latest_movies, name='latest_movie'),
    path('top-rated/', get_top_rated, name='top_rated_movies'),
    path('upcoming/', get_upcoming, name='upcoming_movies')
]
