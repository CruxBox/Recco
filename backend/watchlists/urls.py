from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('', get_watchlists, name='get_watchlists'),
    path('<int:id>/', get_watchlist_details, name='get_watchlist_details'),
    path('<int:id>/add',add_to_watchlist , name='add_to_watchlist'),
    path('<int:id>/remove',remove_from_watchlist,name='remove_from_watchlist'),
]