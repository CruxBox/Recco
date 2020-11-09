
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from backend.app import IncomingApiManager as ApiM


@api_view(('GET',))
def search_movies(request, query, max_results):
	return Response(json.loads(json.dumps(ApiM.search_movies(query, max_results))))


@api_view(('GET',))
def get_popular_movies(request, max_results):
	return Response(json.loads(json.dumps(ApiM.get_popular_movies(max_results))))


@api_view(('GET',))
def get_latest_movies(request):
	return Response(json.loads(json.dumps(ApiM.get_latest_movies())))


@api_view(('GET',))
def get_top_rated(request, max_results):
	return Response(json.loads(json.dumps(ApiM.get_top_rated(max_results))))


@api_view(('GET',))
def get_upcoming(request, max_results):
	return Response(json.loads(json.dumps(ApiM.get_upcoming(max_results))))
