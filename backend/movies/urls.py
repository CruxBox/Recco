from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('search/', search_movies, name='search_movies'),
    path('popular/', get_popular_movies, name='popular_movies'),
    path('latest/', get_latest_movie, name='latest_movie'),
    path('top-rated/', get_top_rated, name='top_rated_movies'),
    path('upcoming/', get_upcoming, name='upcoming_movies'),
    path('comments/all', get_all_comments, name = 'all_comments'),
    path('comments/post', post_comment, name='post_comment'),
    path('comments/', get_all_comments_by_id, name='get_comments_by_id'),
]
