from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import Client, TestCase
from rest_framework.test import APITestCase
from learning_system.users.models import Student, Teacher, StudentProgress, UserComplaint, ReviewsOnTeacher, \
    StudyGroup, User
from learning_system.users.views import StudentSerializer


class TestBase(APITestCase):
    def _create_student(self):
        group_1 = StudyGroup.objects.create()
        response = self.client.post(reverse('users:create_student'), \
            data = {'username':"ivashka", 'password': "password", 'password_confirmation':"password", \
                'study_group': group_1.pk})
        self.assertEqual(response.status_code == 201, True)

    def setUp(self):
        self._create_student()

    def test_user_login(self):
        resp = self.client.post(reverse('users:login_user'), data={'username':"ivashka", 'password': "password"})
        #print(resp.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)



class UserSignOutViewTest(TestBase):
    def setUpExtra(self):
        self.client.login(username='ivashka', password='password')
    
    def test_user_sign_out(self):
        response = self.client.get(reverse('users:logout_user'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
    
class GetAllStudentsTest(TestCase):
    """ Test module for GET all posts API """
    def setUp(self):
        group_1 = StudyGroup.objects.create()
        Student.objects.create(username = 'Stduent #1', study_group=group_1)
        Student.objects.create(username ='Student #2', study_group=group_1)
        Student.objects.create(username='Student #3', study_group=group_1)

    def test_get_all_posts(self):
        # get API response
        response = self.client.get(reverse('users:student_list'))
        # get data from db
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    