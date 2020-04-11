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
from learning_system.practice.models import PracticeCategory
from learning_system.users.models import Student, Teacher, StudentProgress, UserComplaint, ReviewsOnTeacher, StudyGroup, User
from learning_system.users.serializers.student import StudentListSerializer, StudyGroupCreateSerializer
from learning_system.practice.serializers import PracticeTaskCreateSerializer
User = get_user_model()
'''

class TestAdmin(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('user', 'test@mail.ru',
                                                  'user')
        self.client.login(username='user', password='user')
        self.group_1 = StudyGroup.objects.create()
        self.data = {
            'username': "ivashka",
            'first_name': "Ivan",
            'last_name': "Nikolaev",
            'password': "password",
            'password_confirmation': "password",
            'study_group': self.group_1.pk
        }
        self.group_2 = StudyGroup.objects.create()
        self.student = Student.objects.create(username='student',
                                              study_group=self.group_1)

    def test_create_student(self):
        response = self.client.post(reverse('users:student-list'),
                                    data=self.data,
                                    format='json')
        self.assertEqual(response.status_code == 201, True)

    def test_update_student(self):
        response = self.client.put(reverse('users:student-detail',
                                           args=[self.student.pk]),
                                   data={'study_group': self.group_2.pk})
        self.assertEqual(
            Student.objects.get(pk=self.student.pk).study_group.pk,
            self.group_2.pk)

    def test_read_student(self):
        response = self.client.get(reverse('users:student-list'))
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        response = self.client.delete(
            reverse('users:student-detail', args=[self.student.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestTeacher(APITestCase):
    def setUp(self):
        self.user = Teacher.objects.create_user('user', 'test@mail.ru', 'user')
        self.client.login(username='user', password='user')
        self.course_1 = Course.objects.create()
        self.group_1 = StudyGroup.objects.create()
        self.group_2 = StudyGroup.objects.create()
        self.student = Student.objects.create(username='student',
                                              study_group=self.group_1)

    def test_create_student(self):
        data = {
            'username': "ivashka",
            'first_name': "Ivan",
            'last_name': "Nikolaev",
            'password': "password",
            'password_confirmation': "password",
            'study_group': self.group_1.pk
        }
        response = self.client.post(reverse('users:student-list'),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code == 201, True)

    def test_update_student(self):
        response = self.client.put(reverse('users:student-detail',
                                           args=[self.student.pk]),
                                   data={'study_group': self.group_2.pk})
        self.assertEqual(
            Student.objects.get(pk=self.student.pk).study_group.pk,
            self.group_2.pk)

    def test_read_student(self):
        response = self.client.get(reverse('users:student-list'))
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        response = self.client.delete(
            reverse('users:student-detail', args=[self.student.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_study_group(self):
        course_1 = Course.objects.create()
        data = {'name': "group_1", 'available_subjects': course_1.pk}
        response = self.client.post(reverse('users:studygroup-list'),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_study_group(self):
        self.group_1.available_subjects.add(self.course_1)
        course_2 = Course.objects.create()
        response = self.client.put(reverse('users:studygroup-detail',
                                           args=[self.group_1.pk]),
                                   data={
                                       'name': "name",
                                       'available_subjects': course_2.pk
                                   })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_read_study_group(self):
        response = self.client.get(reverse('users:studygroup-list'))
        studygroups = StudyGroup.objects.all()
        serializer = StudyGroupCreateSerializer(studygroups, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_study_group(self):
        response = self.client.delete(
            reverse('users:studygroup-detail', args=[self.group_1.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestStudent(APITestCase):
    def setUp(self):
        self.user = Student.objects.create_user('user', 'test@mail.ru', 'user')
        self.client.login(username='user', password='user')
        self.course_1 = Course.objects.create()
        self.group_1 = StudyGroup.objects.create()
        self.group_2 = StudyGroup.objects.create()

    def test_create_study_group(self):
        course_1 = Course.objects.create()
        data = {'name': "group_1", 'available_subjects': course_1.pk}
        response = self.client.post(reverse('users:studygroup-list'),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_study_group(self):
        self.group_1.available_subjects.add(self.course_1)
        course_2 = Course.objects.create()
        response = self.client.put(reverse('users:studygroup-detail',
                                           args=[self.group_1.pk]),
                                   data={
                                       'name': "name",
                                       'available_subjects': course_2.pk
                                   })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_read_study_group(self):
        response = self.client.get(reverse('users:studygroup-list'))
        studygroups = StudyGroup.objects.all()
        serializer = StudyGroupCreateSerializer(studygroups, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_study_group(self):
        response = self.client.delete(
            reverse('users:studygroup-detail', args=[self.group_1.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestAnonymoususer(APITestCase):
    def setUp(self):
        self.course_1 = Course.objects.create()
        self.group_1 = StudyGroup.objects.create()

    def test_create_study_group(self):
        data = {'name': "group_1", 'available_subjects': self.course_1.pk}
        response = self.client.post(reverse('users:studygroup-list'),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_study_group(self):
        self.group_1 = StudyGroup.objects.create()
        self.group_1.available_subjects.add(self.course_1)
        course_2 = Course.objects.create()
        response = self.client.put(reverse('users:studygroup-detail',
                                           args=[self.group_1.pk]),
                                   data={
                                       'name': "name",
                                       'available_subjects': course_2.pk
                                   })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_read_study_group(self):
        response = self.client.get(reverse('users:studygroup-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_read_delete_group(self):
        response = self.client.delete(
            reverse('users:studygroup-detail', args=[self.group_1.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
'''