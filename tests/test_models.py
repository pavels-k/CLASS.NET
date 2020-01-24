from django.test import TestCase
from learning_system.users.models import User, Student, Group, Teacher
from learning_system.users.models import User, Student, Group, Teacher
from learning_system.courses.models import Course
from learning_system.theory.models import TheoryPost, TheoryCategory
from learning_system.practice.models import PracticeType, PracticeCategory, PracticeTask, PracticeTaskVariation

class UserModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_6(self):
        student_1 = Student.objects.create(username = 'Student #1')
        teacher = Teacher.objects.create(username = 'Teacher #1')
        self.assertEqual(Student.objects.all().count() + Teacher.objects.all() > 1, True)
'''
    def test_1(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        course_2 = Course.objects.create(title = 'ТВиМС')

    def test_2(self):
        course_1 = Course.objects.create(title = 'Математический анализ')
        #course_2 = Course.objects.create(title = 'ТВиМС')
        theorypost_1 = TheoryPost.objects.create(content = 'Текст теоретического материала', course = course_1)
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicetask_1 = PracticeTask.objects.create(content = 'Текст Практического материала материала', practicecategory = practicecategory_1)
        self.assertEqual(theorypost_1.course == course_1, True)
        self.assertEqual(practicecategory_1.course == course_1, True)
'''





'''
    def test_9(self):
        pass


    def test_7(self):
        teacher = Teacher.objects.create(username = 'Din')
        group_1 = Group.objects.create()
        group_1.user.add(teacher)
        group_2 = Group.objects.create()
        group_2.user.add(teacher)
        self.assertEqual((Group.objects.filter(user = teacher).count()) > 1, True)
    
    def test_8(self):
        student = Student.objects.create(username = 'Din')
        group_1 = Group.objects.create()
        group_1.user.add(student)
        group_2 = Group.objects.create()
        group_2.user.add(student)
        self.assertEqual((Group.objects.filter(user = student).count()) == 1, True)

'''
    