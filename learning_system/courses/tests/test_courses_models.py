from django.test import TestCase
from learning_system.courses.models import Course
from learning_system.theory.models import TheoryCategory
from learning_system.practice.models import  PracticeCategory,PracticeTask


class UserModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_ensure_we_can_create_new_course(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        course_2 = Course.objects.create(title = 'ТВиМС')
        self.assertEqual(course_1.title == 'Математический анализ', True)
        self.assertEqual(course_2.title == 'ТВиМС', True)
    
    def test_course_has_theory_and_practice(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        theorycategory_1 = TheoryCategory.objects.create(course = course_1)
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(content = 'Текст Практического материала материала', practicecategory = practicecategory_1)
        self.assertEqual(theorycategory_1.course == course_1, True)
        self.assertEqual(practicecategory_1.course == course_1, True)