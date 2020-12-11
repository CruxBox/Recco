import json

from django.test import TestCase,SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse,resolve
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import path
from movies.views import *



class ApiTestcase(APITestCase):
    def test_registration(self):
        data={"username":"testcase", "email":"test@localhost.app", "password":"some_strong_psw"}
        response=self.client.post("/users/register",data,format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        self.test_registration()
        data={"username":"testcase","password":"some_strong_psw"}
        response=self.client.post("/users/token-auth/login",data,format="json")
        self.token=response.data['token']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def test_movies_watchlist_get(self):
        url="http://127.0.0.1:8000/watchlists/"
        print(url)
        response1=self.test_login()
        print(response1.data)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response1.data['token']) 
        response=self.client.get(url,format="json")
        self.assertEqual(response.status_code,200)

    def test_movies_watchlist_post(self):
        url="http://127.0.0.1:8000/watchlists/"
        print(url)
        response1=self.test_login()
        print(response1.data)
        data={ "name":"temp","description":"test"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response1.data['token']) 
        response=self.client.post(url,data,format="json")
        self.assertEqual(response.status_code,201)
        return response1

    def test_movies_watchlist_put(self):
        url="http://127.0.0.1:8000/watchlists/1/"
        response1=self.test_movies_watchlist_post()
        data={"name":"HEllooo"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response1.data['token'])
        response=self.client.put(url,data,format="json")
        self.assertEqual(response.status_code,200)

    def test_movies_watchlist_get1(self):
        url="http://127.0.0.1:8000/watchlists/1/"
        response1=self.test_movies_watchlist_post()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response1.data['token'])
        response=self.client.get(url,format="json")
        self.assertEqual(response.status_code,200)

    def test_movies_watchlist_delete(self):
        url="http://127.0.0.1:8000/watchlists/1/"
        response1=self.test_movies_watchlist_post()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response1.data['token'])
        response=self.client.delete(url)
        self.assertEqual(response.status_code,204)


    





    