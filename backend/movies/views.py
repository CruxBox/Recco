import json


from django.utils.formats import get_format
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .models import *
from .serializers import *

from backend.app import IncomingApiManager as ApiM

@api_view(('GET',))
@permission_classes((AllowAny,))
def search_movies(request):
	kwargs = dict()
	args = ['max_results', 'language', 'query', 'page', 'include_adult', 'region', 'year', 'primary_release_year']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	kwargs['max_results'] = get_max_results(**kwargs)

	data = ApiM.search_movies(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_popular_movies(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	kwargs['max_results'] = get_max_results(**kwargs)

	data = ApiM.get_popular_movies(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_latest_movie(request):
	kwargs = dict()
	args = ['language']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	kwargs['max_results'] = get_max_results(**kwargs)

	data = ApiM.get_latest_movies(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_top_rated(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	kwargs['max_results'] = get_max_results(**kwargs)

	data = ApiM.get_top_rated(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_upcoming(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	kwargs['max_results'] = get_max_results(**kwargs)

	data = ApiM.get_upcoming(**kwargs)
	return Response(data)


def get_max_results(**kwargs):
    if('max_results' not in kwargs.keys()):
        return 1
    else:
        return int(kwargs['max_results'])


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_all_comments(request):
	comments = Comment.objects.all()
	serializer = CommentSerializer(comments, many = True)
	return Response(serializer.data)


@api_view(('PUT',))
@permission_classes((AllowAny,))
def edit_comment(request, comment_id):
	"""
	Incoming args: movie id
	"""
	try:
		comment = Comment.objects.get(pk = comment_id)
	except Comment.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == "PUT":
		serializer = CommentSerializer(comment, data = request.data)
		data = {}
		if(serializer.is_valid()):
			serializer.save()
			data['success'] = 'update successful'
			return Response(data = data)
	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((AllowAny,))
def delete_comment(request, comment_id):
	"""
	Incoming args: comment_id
	"""
	try:
		comment = Comment.objects.filter(pk = comment_id)
	except Comment.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == "DELETE":
		stat = comment.delete()
		data = {}
		if(stat):
			data['success'] = 'update successful'
		else:
			data['failure'] = 'delete failed'
		return Response(data = data)


@api_view(('POST','GET',))
@permission_classes((AllowAny,))
def get_or_post_comment(request, movie_id):
	"""
	Info for generating movie instance should come from the frontend if request is POST
	That is, [tmdb_id]
	"""
	if request.method == 'POST':
		data = request.data
		try:
			movie = Movie.objects.get(tmdb_id = movie_id)
			print(movie)
		except Movie.DoesNotExist:
			movie = Movie.objects.create(tmdb_id = movie_id)
			movie.save()
			#call a view to fill the movie data. TODO://

		comment = Comment.objects.create(content = data['content'], movie = movie)
		if comment:
			return Response({'success':'successfully posted'}, status = status.HTTP_201_CREATED)
		else:
			return Response({'failure':'failed to create comment'}, status = status.HTTP_400_BAD_REQUEST)
	else:
		"""
		Incoming args: movie id
		"""
		try:
			comments = Comment.objects.filter(movie__tmdb_id = movie_id)
		except Comment.DoesNotExist:
			return Response(status = status.HTTP_404_NOT_FOUND)

		serializer = CommentSerializer(comments, many = True)
		return Response(serializer.data)