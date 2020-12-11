from rest_framework import serializers

from .models import *
from user.models import User
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ['tmdb_id']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username']

class WatchlistsSerializer(serializers.ModelSerializer):
	owner = UserSerializer()
	movies = MovieSerializer(many=True)
	shared_with = UserSerializer(many=True)

	class Meta:
		model = Watchlist
		fields = '__all__'
