from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('search/', search_movies, name='search_movies'),
    path('popular/', get_popular_movies, name='popular_movies'),
    path('latest/', get_latest_movie, name='latest_movie'),
    path('top-rated/', get_top_rated, name='top_rated_movies'),
    path('upcoming/', get_upcoming, name='upcoming_movies'),
    path('search_response_with_tmdb_id/', search_response_with_tmdb_id, name = 'search_response_with_tmdb_id'),
    path('comments/', get_all_comments, name = 'all_comments'),
    path('<int:movie_id>/', get_movie_details, name = 'movie_details'),
    path('<int:movie_id>/comments', get_or_post_comment, name='get_or_post_comment'),
    path('comments/<int:comment_id>', get_comment_by_id, name='get_comment_by_id'),
    path('comments/edit/<int:comment_id>', edit_comment, name = 'edit_comment'),
    path('comments/delete/<int:comment_id>', delete_comment, name = 'delete_comment'),
    path('comments/upvote/<int:comment_id>', upvote_comment, name = 'upvote_comment'),
    path('comments/downvote/<int:comment_id>', downvote_comment, name = 'downvote_comment'),
    path('rec', recommend)
]
