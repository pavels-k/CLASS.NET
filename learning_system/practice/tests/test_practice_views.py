from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from learning_system.practice.models import PracticeCategory, PracticeTask, TaskUserData
from learning_system.courses.models import Course
'''
class UpdatePracticeTask(APITestCase):
    """ Test module for updating an existing post record """
    def setUp(self):
        self.course_1 = Course.objects.create(title='Математический анализ')
        self.practicecategory_1 = PracticeCategory.objects.create(course=self.course_1)
        self.practicetask_1 = PracticeTask.objects.create(content='Текст Практического задания', complexity='Сложный',
                                                     task_type='Тестовая', category=self.practicecategory_1)
    
    def test_create_practice_task(self):
        course_1 = Course.objects.create(title='Математический анализ')
        practice_category_1 = PracticeCategory.objects.create(course=self.course_1)   
        response = self.client.post(reverse('practice:create_practice_task'), \
            data = {'content':"Текст Практического задания", 'complexity': "Сложный", 'task_type':1, \
                'category': practice_category_1.pk})
        #print(response.data)
        self.assertEqual(response.status_code == 201, True)
    
    def test_update_practice_task(self):
        data = {
            "content": "Текст Практического задания",
            "complexity": "Сложный",
            "task_type": 1
        }
        response = self.client.put(reverse('practice:practice_task_update', kwargs={'pk': self.practicetask_1.pk}),\
                                   data=data)
        #print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_practice_task(self):
        response = self.client.delete(reverse('practice:practice_task_update', kwargs={'pk': self.practicetask_1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
'''
