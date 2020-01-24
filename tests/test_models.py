from django.test import TestCase
from learning_system.users.models import User, Student, Group, Teacher, group_validate,UserProgress
from learning_system.courses.models import Course
from learning_system.theory.models import TheoryPost, TheoryCategory
from learning_system.practice.models import PracticeType, PracticeCategory, PracticeTask, PracticeTaskVariation
from django.core.exceptions import ValidationError

class UserModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_1(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        course_2 = Course.objects.create(title = 'ТВиМС')

    def test_2(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        theorypost_1 = TheoryPost.objects.create(content = 'Текст теоретического материала', course = course_1)
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(content = 'Текст Практического материала материала', practicecategory = practicecategory_1)
        self.assertEqual(theorypost_1.course == course_1, True)
        self.assertEqual(practicecategory_1.course == course_1, True)
    
    def test_5(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(content = 'Текст Практического материала', complexity = 'Сложный',type_task = 'Тестовая', practicecategory = practicecategory_1)
    
    def test_6(self):
        teacher_1 = Teacher.objects.create(username = 'Teacher #1')
        student_1 = Student.objects.create(username = 'Student #1')
        self.assertEqual(Student.objects.all().count() + Teacher.objects.all().count() > 1, True)
    
    def test_7(self):
        teacher_1 = Teacher.objects.create(username = 'Teacher #1')
        group_1 = Group.objects.create()
        group_2 = Group.objects.create()
        teacher_1.groups.add(group_1, group_2)
        self.assertEqual(teacher_1.groups.all().count() > 1, True)
    
    def test_8(self):
        student_1 = Student.objects.create(username = 'Student #1')
        user_1 = User.objects.create(username = 'User #1')
        group_1 = Group.objects.create()
        group_2 = Group.objects.create()
        student_1.groups.add(group_1, group_2)
        #group_validate(student_1)
        #self.assertEqual(student_1.groups.all().count() == 0, True)
    
    def test_9(self):
        teacher_1 = Teacher.objects.create(username = 'Teacher #1')
        group_1 = Group.objects.create()
        teacher_1.groups.add(group_1)
        course_1 = Course.objects.create()
        course_2 = Course.objects.create()
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(practicecategory = practicecategory_1)
        userprogress = UserProgress.objects.create(user = teacher_1, score = 0, practicetask = practicetask_1)

    

