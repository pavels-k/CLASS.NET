
from django.test import TestCase
from learning_system.courses.models import Course
from learning_system.theory.models import TheoryCategory, TheoryPost


class TheoryModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass
        
    def test_theory_has_sections_and_subsections(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        theorycategory_1 = TheoryCategory.objects.create(course = course_1)
        theorycategory_sub_1 = TheoryCategory.objects.create(course = course_1)        
        theorycategory_subsection_1 = TheoryCategory.objects.create(course = course_1, parent = theorycategory_sub_1)        
        theorytask_section_1 = TheoryPost.objects.create( content = 'Теория раздела', category = theorycategory_sub_1)
        theorytask_subsection_1 = TheoryPost.objects.create(content = 'Теория подраздела', category = theorycategory_subsection_1)
        self.assertEqual(theorytask_section_1.content == 'Теория раздела', True)
        self.assertEqual(theorytask_subsection_1.content == 'Теория подраздела', True)
