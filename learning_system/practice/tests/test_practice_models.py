from django.test import TestCase
from learning_system.courses.models import Course
from learning_system.users.models import Student
from learning_system.practice.models import PracticeCategory, PracticeTask, TaskUserData


class PracticeModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass
        
    def test_practice_task_has_text_complexity_and_type(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(content = 'Текст Практического задания', complexity = 'Сложный',type_task = 'Тестовая', category = practicecategory_1)
        self.assertEqual(practicetask_1.content == 'Текст Практического задания' and practicetask_1.complexity == 'Сложный' and practicetask_1.type_task == 'Тестовая', True)

    def test_practice_has_sections_and_subsections(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicecategory_sub_1 = PracticeCategory.objects.create(course = course_1, parent = practicecategory_1)        
        practicetask_section_1 = PracticeTask.objects.create( type_task = 'Тестовая', category = practicecategory_1)
        practicetask_subsection_1 = PracticeTask.objects.create(type_task = 'Письменный', category = practicecategory_sub_1)
        self.assertEqual(practicetask_section_1.type_task == 'Тестовая', True)
        self.assertEqual(practicetask_subsection_1.type_task == 'Письменный', True)
    
    def test_take_into_account_the_number_of_tries(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(content = 'Текст Практического задания', complexity = 'Сложный',type_task = 'Тестовая', category = practicecategory_1)
        student_1 = Student.objects.create(username = 'Student #1')
        taskuserdata_1 = TaskUserData.objects.create(student = student_1, practicetask = practicetask_1)
        TaskUserData.add_new_try(taskuserdata_1)
        self.assertEqual(taskuserdata_1.tries_count > 0, True)


    
