from django.test import TestCase
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
from learning_system.users.serializers.student import StudentListSerializer, GetTaskListSerializer



class TestBase(APITestCase):
    def _create_student(self):
        group_1 = StudyGroup.objects.create()

        response = self.client.post('/core/v1/users/student/create/', \
            data = {'username':"ivashka", 'first_name':"Ivan",'last_name': "Nikolaev", 'password': "password", 'password_confirmation':"password", \
                'study_group': group_1.pk})
        self.assertEqual(response.status_code == 201, True)

    def setUp(self):
        self._create_student()

    def test_user_login(self):
        resp = self.client.post(reverse('users:login_user'),
                                data={
                                    'username': "ivashka",
                                    'password': "password"
                                })
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class UserSignOutViewTest(TestBase):
    def setUpExtra(self):
        a = self.client.login(username='ivashka', password='password')
        print(a)

    def test_user_sign_out(self):
        response = self.client.get(reverse('users:logout_user'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class GetAllStudentsTest(TestCase):
    def _create_student(self):
        group_1 = StudyGroup.objects.create()
        response = self.client.post('/core/v1/users/student/create/', \
            data = {'username':"ivashka", 'first_name':"Ivan",'last_name': "Nikolaev", 'password': "password", 'password_confirmation':"password", \
                'study_group': group_1.pk})

        self.assertEqual(response.status_code == 201, True)

    def _create_teacher(self):
        group_1 = StudyGroup.objects.create()
        response = self.client.post('/core/v1/users/teacher/create/', \
            data = {'username':"platonov", 'first_name':"Evgen",'last_name': "Platonov", 'password': "password", 'password_confirmation':"password", \
                'study_groups': group_1.pk})

        self.assertEqual(response.status_code == 201, True)

    def _create_admin(self):
        my_admin = User.objects.create_superuser('ADMIN', 'myemail@test.com',
                                                 'password')


    def setUp(self):
        group_1 = StudyGroup.objects.create()
        Student.objects.create(username='Stduent #1', study_group=group_1)
        Student.objects.create(username='Student #2', study_group=group_1)
        Student.objects.create(username='Student #3', study_group=group_1)
        self._create_student()
        self._create_teacher()
        self._create_admin()

    def test_get_all_students(self):
        response = self.client.get('/core/v1/users/student/list/')
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_list(self):
        c = Client()
        c.login(username='ivashka', password='password')
        student = Student.objects.get(username='ivashka')
        course_1 = Course.objects.create(title='Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course=course_1)
        practicetask_1 = PracticeTask.objects.create(
            content='Текст Практического задания',
            complexity='Сложный',
            task_type='Тестовая',
            category=practicecategory_1)

        student_progress = StudentProgress.objects.create(
            practice_task=practicetask_1,
            score=0,
            answers='Ответы',
            student=student)
        serializer = GetTaskListSerializer(practicetask_1)
        response = c.get('/core/v1/users/get_task_list_for_student/')
        self.assertEqual(response.status_code, 200)

    def test_set_group_for_student(self):
        c = APIClient()
        c.login(username='platonov', password='password')
        student = Student.objects.get(username='ivashka')
        study_group = StudyGroup.objects.create(name='404')
        response = c.put(
            '/core/v1/users/set_group_for_student/' + str(student.pk) + '/',
            {"study_group": study_group.pk})
        student = Student.objects.get(username='ivashka')
        self.assertEqual(student.study_group, study_group)

    def test_add_group_to_study_group(self):
        c = APIClient()
        c.login(username='ADMIN', password='password')
        course = Course.objects.create(title='Математический анализ')
        study_group = StudyGroup.objects.create(name='404')
        response = c.put(
            '/core/v1/users/add_study_group_to_course/' + str(study_group.pk) +
            '/', {"available_subjects": course.pk})
        self.assertEqual(study_group.available_subjects.all().exists(), True)

    def test_get_result_for_group(self):
        c = APIClient()
        c.login(username='platonov', password='password')

        group_1 = StudyGroup.objects.create(name='group_1')
        group_2 = StudyGroup.objects.create(name='group_2')
        group_3 = StudyGroup.objects.create(name='group_3')
        student_1 = Student.objects.create(username='student_1',
                                           study_group=group_3)

        course_1 = Course.objects.create()
        practicecategory_1 = PracticeCategory.objects.create(course=course_1)
        practicetask_1 = PracticeTask.objects.create(
            category=practicecategory_1)
        studentprogress_1 = StudentProgress.objects.create(
            student=student_1, score=0, practice_task=practicetask_1)

        response = c.get('/core/v1/users/get/results/study_group/' +
                         str(group_3.pk))
        self.assertEqual(response.status_code, 200)

    def test_get_progress_for_course_and_group(self):
        c = APIClient()
        c.login(username='platonov', password='password')

        course_1 = Course.objects.create(title='Матан')
        course_2 = Course.objects.create(title='ТВиМС')
        practicecategory_1 = PracticeCategory.objects.create(course=course_2)
        group_1 = StudyGroup.objects.create(name='group_1')
        group_2 = StudyGroup.objects.create(name='group_2')
        group_3 = StudyGroup.objects.create(name='group_3')
        group_3.available_subjects.add(course_2)
        student_1 = Student.objects.create(username='student_1',
                                           study_group=group_3)
        practicetask_1 = PracticeTask.objects.create(
            category=practicecategory_1)
        studentprogress_1 = StudentProgress.objects.create(
            student=student_1, score=0, practice_task=practicetask_1)
        response = c.get('/core/v1/users/students/get_progress/?&group=' +
                         str(group_3.pk) + '&course=' + str(course_2.pk))
        self.assertEqual(response.status_code, 200)
