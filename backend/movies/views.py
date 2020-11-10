import json

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
def get_all_comments_by_id(request):
	"""
	Incoming args: movie id
	"""
	id = kwargs['tmdb_id']
	comments = Comment.objects.filter(tmdb_id = id)
	serializer = CommentSerializer(comments, many = True)
	return Response(serializer.data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_all_comments(request):
	comments = Comment.objects.all()
	serializer = CommentSerializer(comments, many = True)
	return Response(serializer.data)


@api_view(('POST',))
@permission_classes((AllowAny,))
def post_comment(request):
	"""
	Info for generating movie instance should come from the frontend.
	That is, [id, imdb_id, vote_average, vote_count, popularity]
	"""
	serializer = CommentSerializer(data = request.DATA)
	if serializer.is_valid():
		# TODO://Generate the movie instance here.
		# Do we do request.DATA['someKey'] to get the data?
		serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
