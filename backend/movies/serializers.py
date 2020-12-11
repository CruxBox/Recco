from rest_framework import serializers

from .models import *
from user.serializers import *

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['content', 'created','score','user','movie']

	def to_representation(self, instance):
		return {
			'content': instance.content,
			'created': instance.created,
			'score': instance.score,
			'tmdb_id': instance.movie.tmdb_id,
			'username': instance.user.username
		}

class MoviesSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(many = True)
	class Meta:
		model = Movie
		fields = ['__all__', 'comments']