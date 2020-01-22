from django.test import TestCase
from learning_system.users.models import User, Student, Group, group_validate

class UserModelTest(TestCase):

    @classmethod
    def setUp(self):
        self.id1 = User.objects.create(username='Иван')
        self.id2 = User.objects.create(username='Ivan')
        self.st1 = Student.objects.create(username = 'din')
        self.st2 = Student.objects.create(username = 'greg')
        
        Group.objects.create(student_id = 1, name = '404')


    def test_publish_method_for_post(self):
        gruppa = Group.objects.get(title='Blog Post #1')
        #self.assertEqual(, True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1+1, 2)
    