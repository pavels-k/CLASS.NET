from django.test import TestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import Client, TestCase
import json
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate, login, logout
from learning_system.courses.models import Course
from learning_system.practice.models import PracticeCategory, PracticeTask, TaskUserData
from learning_system.users.models import Student, Teacher, StudentProgress, UserComplaint, ReviewsOnTeacher, \
    StudyGroup, User
from learning_system.users.serializers.student import StudentListSerializer
from learning_system.practice.serializers import PracticeTaskCreateSerializer
User = get_user_model()

class TestBase(APITestCase):
    def _create_student(self):
        client = APIClient()
        print(client)
        print(client.login(username='ADMIN', password='password'))
        print(client)
        group_1 = StudyGroup.objects.create()
        data = {'username':"ivashka", 'first_name':"Ivan",'last_name': "Nikolaev", 'password': "password", 'password_confirmation':"password", \
                'study_group': group_1.pk}

        response = client.post(reverse('users:student-list'), data = data, format='json')
        print(response.data)
        self.assertEqual(response.status_code == 201, True)

    def setUp(self):
        my_admin = User.objects.create_superuser('ADMIN', 'myemail@test.com',
                                                 'password')
        self._create_student()

    def test_user_login(self):
        resp = self.client.post(reverse('users:login_user'),
                                data={
                                    'username': "ivashka",
                                    'password': "password"
                                })
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

'''
class MemberTests(APITestCase):
    def test_api_jwt(self):

        url = '/core/v1/users/api/token'
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        u.is_active = False
        u.save()

        resp = self.client.post(url, {'email':'user@foo.com', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        u.is_active = True
        u.save()

        resp = self.client.post(url, {'username':'user@foo.com', 'password':'pass'}, format='json')
        print(resp.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']
        #print(token)

        verification_url = reverse('api-jwt-verify')
        resp = self.client.post(verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
'''