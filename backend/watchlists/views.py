from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


from .models import *
from .serializers import *


@api_view(('GET','POST'))
@authentication_classes((TokenAuthentication, ))
def get_watchlists(request):
    if request.method == "GET":
        user = request.user
        watchlists = Watchlist.objects.all().filter(owner=user)
        response = WatchlistsSerializer(watchlists,many=True)
        return Response(response.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data 
        user = request.user
        watchlist = Watchlist.objects.create(name=data['name'],description=data['description'],owner=user)
        response = WatchlistsSerializer(watchlist)
        return Response(response.data,status=status.HTTP_201_CREATED)




@api_view(('GET',))
@authentication_classes((TokenAuthentication, ))
def get_watchlist_details(request, id):
    if request.method == "GET":
        try:
            watchlists = Watchlist.objects.get(id=id)
            response = WatchlistsSerializer(watchlists)
            return Response(response.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
