from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('', get_watchlists, name='get_watchlists'),
    path('<int:id>/', get_watchlist_details, name='get_watchlist_details'),
]