from django.test import TestCase

from learning_system.courses.models import Course
from learning_system.practice.models import PracticeCategory, AbstractTask, FormulInputTask, FormulInputTaskVariation 
from learning_system.users.models import Student, StudyGroup


class PracticeModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass
        
    def test_abstract_task(self):
        #abstracttask = AbstractTask.objects.create()
        formul = FormulInputTask.objects.create()
        #print(AbstractTask.objects.all())

'''
    def test_practice_task_has_text_complexity_and_type(self):
        course_1 = Course.objects.create(title='Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course=course_1)
        practicetask_1 = PracticeTask.objects.create(content='Текст Практического задания', complexity='Сложный',
                                                     task_type='Тестовая', category=practicecategory_1)
        self.assertEqual(
            practicetask_1.content == 'Текст Практического задания' and practicetask_1.complexity == 'Сложный' and practicetask_1.task_type == 'Тестовая',
            True)

    def test_practice_has_sections_and_subsections(self):
        course_1 = Course.objects.create(title='Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course=course_1)
        practicecategory_sub_1 = PracticeCategory.objects.create(course=course_1, parent=practicecategory_1)
        practicetask_section_1 = PracticeTask.objects.create(task_type='Тестовая', category=practicecategory_1)
        practicetask_subsection_1 = PracticeTask.objects.create(task_type='Письменный', category=practicecategory_sub_1)
        self.assertEqual(practicetask_section_1.task_type == 'Тестовая', True)
        self.assertEqual(practicetask_subsection_1.task_type == 'Письменный', True)

    def test_take_into_account_the_number_of_tries(self):
        course_1 = Course.objects.create(title='Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course=course_1)
        practicetask_1 = PracticeTask.objects.create(content='Текст Практического задания', complexity='Сложный',
                                                     task_type='Тестовая', category=practicecategory_1)
        taskuserdata_1 = TaskUserData.objects.create(practice_task=practicetask_1)
        TaskUserData.add_new_try(taskuserdata_1)
        self.assertEqual(taskuserdata_1.tries_count > 0, True)
'''