import json

from django.test import TestCase,SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse,resolve
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import path
from user.views import login,logout,RegisterAPI

from user.serializers import RegisterSerializer

class UrlTest(SimpleTestCase):

    def test_admin(self):
        response=self.client.get("/admin",{},True)
        self.assertEqual(response.status_code,200)

    def test_register(self):
        self.assertEqual(resolve("/users/register").func.view_class, RegisterAPI)

    def test_login(self):
        self.assertEqual(resolve("/users/token-auth/login").func, login)

    def test_logout(self):
        self.assertEqual(resolve("/users/token-auth/logout").func, logout)
        
class ApiTest(APITestCase):

    token = None

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

    def test_logout(self):
        self.test_login()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token) 
        response=self.client.delete("/users/token-auth/logout")
        self.assertEqual(response.status_code, status.HTTP_200_OK)