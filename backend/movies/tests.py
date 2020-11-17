import json

from django.test import TestCase,SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse,resolve
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import path
from movies.views import *

class UrlTest(SimpleTestCase):
    def test_search_movies(self):
        url=reverse('search_movies')
        self.assertEqual(resolve(url).func,search_movies )
    def test_popular_movies(self):
        url=reverse('popular_movies')
        self.assertEqual(resolve(url).func,get_popular_movies )
    def test_latest_movie(self):
        url=reverse('latest_movie')
        self.assertEqual(resolve(url).func,get_latest_movie )
    def test_top_rated_movies(self):
        url=reverse('top_rated_movies')
        self.assertEqual(resolve(url).func,get_top_rated )
    def test_upcoming_movies(self):
        url=reverse('upcoming_movies')
        self.assertEqual(resolve(url).func,get_upcoming )
    def test_all_comments(self):
        url=reverse('all_comments')
        self.assertEqual(resolve(url).func,get_all_comments )
    def test_movie_details(self):
        url=reverse('movie_details',args=['1'])
        self.assertEqual(resolve(url).func,get_movie_details )
    def test_register(self):
        url=reverse('get_or_post_comment',args=['1'])
        self.assertEqual(resolve(url).func,get_or_post_comment )
    def test_get_or_post_comment(self):
        url=reverse('get_comment_by_id',args=['1'])
        self.assertEqual(resolve(url).func,get_comment_by_id )
    def test_edit_comment(self):
        url=reverse('edit_comment',args=['1'])
        self.assertEqual(resolve(url).func,edit_comment )
    def test_delete_comment(self):
        url=reverse('delete_comment',args=['1'])
        self.assertEqual(resolve(url).func,delete_comment )
    def test_upvote_comment(self):
        url=reverse('upvote_comment',args=['1'])
        self.assertEqual(resolve(url).func,upvote_comment )
    def test_downvote_comment(self):
        url=reverse('downvote_comment',args=['1'])
        self.assertEqual(resolve(url).func,downvote_comment )


    