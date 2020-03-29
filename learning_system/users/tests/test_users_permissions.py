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
from learning_system.users.models import Student, Teacher, StudentProgress, UserComplaint, ReviewsOnTeacher, StudyGroup, User
from learning_system.users.serializers.student import StudentListSerializer, StudyGroupCreateSerializer
from learning_system.practice.serializers import PracticeTaskCreateSerializer
User = get_user_model()


class TestAdmin(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('user', 'test@mail.ru',
                                                  'user')
        self.client.login(username='user', password='user')

    def test_CRUD_student(self):
        group_1 = StudyGroup.objects.create()
        data = {
            'username': "ivashka",
            'first_name': "Ivan",
            'last_name': "Nikolaev",
            'password': "password",
            'password_confirmation': "password",
            'study_group': group_1.pk
        }
        response = self.client.post(reverse('users:student-list'),
                                    data=data,
                                    format='json')
        pk = response.data.get('id')
        self.assertEqual(response.status_code == 201, True)

        group_2 = StudyGroup.objects.create()
        response = self.client.put(reverse('users:student-detail', args=[pk]),
                                   data={'study_group': group_2.pk})
        self.assertEqual(Student.objects.get(pk=pk).study_group.pk, group_2.pk)

        response = self.client.get(reverse('users:student-list'))
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(
            reverse('users:student-detail', args=[pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestTeacher(APITestCase):
    def setUp(self):
        self.user = Teacher.objects.create_user('user', 'test@mail.ru', 'user')
        self.client.login(username='user', password='user')

    def test_CRUD_student(self):
        group_1 = StudyGroup.objects.create()
        data = {
            'username': "ivashka",
            'first_name': "Ivan",
            'last_name': "Nikolaev",
            'password': "password",
            'password_confirmation': "password",
            'study_group': group_1.pk
        }
        response = self.client.post(reverse('users:student-list'),
                                    data=data,
                                    format='json')
        pk = response.data.get('id')
        self.assertEqual(response.status_code == 201, True)

        group_2 = StudyGroup.objects.create()
        response = self.client.put(reverse('users:student-detail', args=[pk]),
                                   data={'study_group': group_2.pk})
        self.assertEqual(Student.objects.get(pk=pk).study_group.pk, group_2.pk)

        response = self.client.get(reverse('users:student-list'))
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(
            reverse('users:student-detail', args=[pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_CRUD_study_group(self):
        course_1 = Course.objects.create()
        data = {'name': "group_1", 'available_subjects': course_1.pk}
        response = self.client.post(reverse('users:studygroup-list'),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        study_group = StudyGroup.objects.create()
        study_group.available_subjects.add(course_1)
        course_2 = Course.objects.create()
        response = self.client.put(reverse('users:studygroup-detail',
                                           args=[study_group.pk]),
                                   data={
                                       'name': "name",
                                       'available_subjects': course_2.pk
                                   })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.get(reverse('users:studygroup-list'))
        studygroups = StudyGroup.objects.all()
        serializer = StudyGroupCreateSerializer(studygroups, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(
            reverse('users:studygroup-detail', args=[study_group.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestStudent(APITestCase):
    def setUp(self):
        self.user = Student.objects.create_user('user', 'test@mail.ru', 'user')
        self.client.login(username='user', password='user')

    def test_CRUD_study_group(self):
        course_1 = Course.objects.create()
        data = {'name': "group_1", 'available_subjects': course_1.pk}
        response = self.client.post(reverse('users:studygroup-list'),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        study_group = StudyGroup.objects.create()
        study_group.available_subjects.add(course_1)
        course_2 = Course.objects.create()
        response = self.client.put(reverse('users:studygroup-detail',
                                           args=[study_group.pk]),
                                   data={
                                       'name': "name",
                                       'available_subjects': course_2.pk
                                   })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.get(reverse('users:studygroup-list'))
        studygroups = StudyGroup.objects.all()
        serializer = StudyGroupCreateSerializer(studygroups, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(
            reverse('users:studygroup-detail', args=[study_group.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestAnonymoususer(APITestCase):
    def test_CRUD_study_group(self):
        course_1 = Course.objects.create()
        data = {'name': "group_1", 'available_subjects': course_1.pk}
        response = self.client.post(reverse('users:studygroup-list'),
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        study_group = StudyGroup.objects.create()
        study_group.available_subjects.add(course_1)
        course_2 = Course.objects.create()
        response = self.client.put(reverse('users:studygroup-detail',
                                           args=[study_group.pk]),
                                   data={
                                       'name': "name",
                                       'available_subjects': course_2.pk
                                   })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.get(reverse('users:studygroup-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(
            reverse('users:studygroup-detail', args=[study_group.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)