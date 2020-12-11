from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


from .models import *
from movies.models import *
from .serializers import *


@api_view(('GET', 'POST'))
@authentication_classes((TokenAuthentication, ))
def get_watchlists(request):
    if request.method == "GET":
        user = request.user
        owned_watchlists = user.get_owned_watchlists()
        shared_watchlists = user.get_shared_watchlists()
        response = dict()
        response['owned'] = WatchlistsSerializer(
            owned_watchlists, many=True).data
        response['shared'] = WatchlistsSerializer(
            shared_watchlists, many=True).data
        return Response(response, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        user = request.user
        watchlist = Watchlist.objects.create(
            name=data['name'], description=data['description'], owner=user)
        response = WatchlistsSerializer(watchlist)
        return Response(response.data, status=status.HTTP_201_CREATED)


@api_view(('DELETE', 'GET', 'PUT'))
@authentication_classes((TokenAuthentication, ))
def get_watchlist_details(request, id):
    watchlist = get_object_or_404(Watchlist, id=id)
    if request.method == "GET":
        try:
            response = WatchlistsSerializer(watchlist)
            if request.user != watchlist.owner or request.user not in watchlist.shared_with.all():
                return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(response.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        try:
            if request.user != watchlist.owner:
                return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)
            watchlist.delete()
            return Response({"message": "Succesfully Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "PUT":
        try:
            if request.user != watchlist.owner:
                return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)
            data = request.data
            if 'name' in data:
                watchlist.name = data['name']
            if 'description' in data:
                watchlist.description = data['description']
            watchlist.save()
            response = WatchlistsSerializer(watchlist)
            return Response(response.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(('PATCH',))
@authentication_classes((TokenAuthentication, ))
def add_to_watchlist(request, id):
    if request.method == "POST":
        try:
            data = request.data
            watchlist = Watchlist.objects.get(id=id)
            for movie_id in data['movies']:
                movie = Movie.objects.get(tmdb_id=movie_id['tmdb_id'])
                watchlist.movies.add(movie)
            response = WatchlistsSerializer(watchlist)
            return Response(response.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(('PATCH',))
@authentication_classes((TokenAuthentication, ))
def remove_from_watchlist(request, id):
    if request.method == "DELETE":
        try:
            data = request.data
            watchlist = Watchlist.objects.get(id=id)
            for movie_id in data['movies']:
                movie = Movie.objects.get(tmdb_id=movie_id['tmdb_id'])
                watchlist.movies.remove(movie)
            response = WatchlistsSerializer(watchlist)
            return Response(response.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(('PATCH',))
@authentication_classes((TokenAuthentication, ))
def share_watchlist(request, id):
    watchlist = get_object_or_404(Watchlist, id=id)
    if request.user != watchlist.owner:
        return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        data = request.data
        if 'users' not in data:
            return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)
        # for id_ in data['users']:
        users = User.objects.filter(id__in=data['users'])
        watchlist.shared_with.add(*list(users))
        response = WatchlistsSerializer(watchlist)
        return Response(response.data, status=status.HTTP_201_CREATED)


@api_view(('PATCH',))
@authentication_classes((TokenAuthentication, ))
def unshare_watchlist(request, id):
    watchlist = get_object_or_404(Watchlist, id=id)
    if request.user != watchlist.owner:
        return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        data = request.data
        if 'users' not in data:
            return Response({'error': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)
        users = User.objects.filter(id__in=data['users'])
        watchlist.shared_with.remove(*list(users))
        response = WatchlistsSerializer(watchlist)
        return Response(response.data, status=status.HTTP_201_CREATED)
