
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from backend.app import IncomingApiManager as ApiM


@api_view(('GET',))
@permission_classes((AllowAny,))
def search_movies(request):
	kwargs = dict()
	args = ['max_results', 'language', 'query', 'page', 'include_adult', 'region', 'year', 'primary_release_year']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)
	data = ApiM.search_movies(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_popular_movies(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)
	data = ApiM.get_popular_movies(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_latest_movies(request):
	kwargs = dict()
	args = ['language']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)
	data = ApiM.get_latest_movies(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_top_rated(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)
	data = ApiM.get_top_rated(**kwargs)
	return Response(data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_upcoming(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)
	data = ApiM.get_upcoming(**kwargs)
	return Response(data)