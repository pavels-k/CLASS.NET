from django.test import TestCase
from learning_system.courses.models import Course
from learning_system.practice.models import PracticeCategory, PracticeTask


class UserModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass
    def test_practice_task_has_text_complexity_and_type(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(content = 'Текст Практического материала', complexity = 'Сложный',type_task = 'Тестовая', practicecategory = practicecategory_1)
        self.assertEqual(practicetask_1.content == 'Текст Практического материала' and practicetask_1.complexity == 'Сложный' and practicetask_1.type_task == 'Тестовая', True)