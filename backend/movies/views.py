
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from backend.app import IncomingApiManager as ApiM


@api_view(('GET',))
def search_movies(request):
	kwargs = dict()
	args = ['max_results', 'language', 'query', 'page', 'include_adult', 'region', 'year', 'primary_release_year']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	return Response(json.loads(json.dumps(ApiM.search_movies(kwargs))))


@api_view(('GET',))
def get_popular_movies(request):

	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	return Response(json.loads(json.dumps(ApiM.get_popular_movies(kwargs))))


@api_view(('GET',))
def get_latest_movies(request):
	kwargs = dict()
	args = ['language']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	return Response(json.loads(json.dumps(ApiM.get_latest_movies(kwargs))))


@api_view(('GET',))
def get_top_rated(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	return Response(json.loads(json.dumps(ApiM.get_top_rated(kwargs))))


@api_view(('GET',))
def get_upcoming(request):
	kwargs = dict()
	args = ['max_results', 'language', 'page', 'region']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	return Response(json.loads(json.dumps(ApiM.get_upcoming(kwargs))))