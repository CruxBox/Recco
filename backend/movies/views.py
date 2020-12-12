import json
import numpy as np 
import pandas as pd

from django.utils.formats import get_format
from django.db.models import Case, When
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .models import *
from .serializers import *

from backend.app import IncomingApiManager as ApiM
from .recom import *

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

@api_view(('GET',))
@permission_classes((AllowAny,))
def get_movie_details(request,movie_id):
	try:
		movie = Movie.objects.get(tmdb_id = movie_id)
		status_ = status.HTTP_200_OK
	except Movie.DoesNotExist:
		movie = Movie.objects.create(tmdb_id = movie_id)
		movie.save()	
		status_ = status.HTTP_201_CREATED
	data = ApiM.get_movie_details(movie_id)
	return Response(data,status=status_)


def get_max_results(**kwargs):
    if('max_results' not in kwargs.keys()):
        return 1
    elif kwargs['max_results'] == None:
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
@authentication_classes((TokenAuthentication, ))
def edit_comment(request, comment_id):
	"""
	Incoming args: movie id
	"""
	try:
		comment = Comment.objects.get(pk = comment_id)
	except Comment.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.user != comment.user:
		return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)

	if request.method == "PUT":
		tempData = request.data.copy()
		tempData['user'] = comment.user.pk
		tempData['movie'] = comment.movie.pk
		serializer = CommentSerializer(comment, data = tempData)
		data = {}
		if(serializer.is_valid()):
			serializer.save()
			data['success'] = 'update successful'
			return Response(data = data)
	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes((AllowAny,))
@authentication_classes((TokenAuthentication, ))
def delete_comment(request, comment_id):
	"""
	Incoming args: comment_id
	"""
	try:
		comment = Comment.objects.get(pk = comment_id)
	except Comment.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.user != comment.user:
			return Response({'details': 'You do not have the permission'}, status=status.HTTP_401_UNAUTHORIZED)

	if request.method == "DELETE":
		stat = comment.delete()
		data = {}
		if(stat):
			data['success'] = 'delete successful'
		else:
			data['failure'] = 'delete failed'
		return Response(data = data)


@api_view(('POST','GET',))
@permission_classes((AllowAny,))
@authentication_classes((TokenAuthentication, ))
def get_or_post_comment(request, movie_id):
	"""
	Info for generating movie instance should come from the frontend if request is POST
	That is, [tmdb_id]
	"""
	try:
		movie = Movie.objects.get(tmdb_id = movie_id)
		print(movie)
	except Movie.DoesNotExist:
		data = ApiM.get_movie_details(movie_id)
		movie = Movie.objects.create(tmdb_id = movie_id)
		#call a view to fill the movie data. TODO://
	if request.method == 'POST':
		data = request.data
		comment = Comment.objects.create(content = data['content'], movie = movie, user = request.user)
		if comment:
			return Response({'success':'successfully posted'}, status = status.HTTP_201_CREATED)
		else:
			return Response({'failure':'failed to create comment'}, status = status.HTTP_400_BAD_REQUEST)
	else:
		"""
		Incoming args: movie id
		"""
		try:
			comments = Comment.objects.filter(movie = movie.pk)
		except Comment.DoesNotExist:
			return Response(status = status.HTTP_404_NOT_FOUND)
		serializer = CommentSerializer(comments, many = True)
		return Response(serializer.data)


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_comment_by_id(request, comment_id):
	try:
		comment = Comment.objects.get(pk = comment_id)
	except Comment.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	serializer = CommentSerializer(comment)
	return Response(serializer.data)


@api_view(('POST',))
@permission_classes((AllowAny,))
def upvote_comment(request, comment_id):
	try:
		comment = Comment.objects.get(pk = comment_id)
	except Comment.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if comment:
		#Change contribution of comment owner. TODO://
		comment.score += 1;
		comment.save()
		return Response({'success':'successfully upvoted'})
	else:
		return Response({'failure':'failed to upvote'}, status = status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@permission_classes((AllowAny,))
def downvote_comment(request, comment_id):
	try:
		comment = Comment.objects.get(pk = comment_id)
	except Comment.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if comment:
		#Change contribution of comment owner. TODO://
		comment.score -= 1;
		comment.save()
		return Response({'success':'successfully downvoted'})
	else:
		return Response({'failure':'failed to downvote'}, status = status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@permission_classes((AllowAny,))
def search_response_with_tmdb_id(request):
	kwargs = dict()
	args = ['query', 'tmdb_id']
	for arg in args:
		kwargs[arg] = request.query_params.get(arg, None)

	data = ApiM.search_response_with_tmdb_id(**kwargs)
	return Response(data)

# for recommendation
@api_view(('GET',))
@permission_classes((AllowAny,))
def recommend(request):
	username = request.query_params.get('username', None)
	if username == None:
		return Response({'Error':'Provide username'}, status = status.HTTP_400_BAD_REQUEST)
	df=pd.DataFrame(list(Rating.objects.all().values()))
	nu=df.user_id.unique().shape[0]
	try:
		user = User.objects.get(username = username)
	except User.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	current_user_id = user.id
	# if new user not rated any movie
	if current_user_id>nu:
		movie=Movie.objects.get(id=1)
		q=Rating(user=user,movie=movie,rating=0)
		q.save()

	print("Current user id: ",current_user_id)
	prediction_matrix,Ymean = Myrecommend()
	my_predictions = prediction_matrix[:,current_user_id-1]+Ymean.flatten()
	pred_idxs_sorted = np.argsort(my_predictions)
	pred_idxs_sorted[:] = pred_idxs_sorted[::-1]
	pred_idxs_sorted=pred_idxs_sorted+1
	preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pred_idxs_sorted)])
	movie_list=list(Movie.objects.filter(id__in = pred_idxs_sorted,).order_by(preserved)[:10])
	serializer = MoviesSerializer(movie_list, many = True)
	return Response(serializer.data)