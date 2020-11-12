from rest_framework import serializers

from .models import *


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['content', 'created','score']

class MoviesSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(many = True)
	class Meta:
		model = Movie
		fields = ['__all__', 'comments']