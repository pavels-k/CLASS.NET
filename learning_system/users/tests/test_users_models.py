from django.test import TestCase
from learning_system.users.models import User, Student, Group, Teacher, group_validate,UserProgress, UserComplaint,ReviewsOnTeacher
from learning_system.courses.models import Course
from learning_system.theory.models import TheoryPost, TheoryCategory
from learning_system.practice.models import PracticeCategory, PracticeTask
from django.core.exceptions import ValidationError

class UserModelTest(TestCase):

    @classmethod
    def setUp(cls):
        pass
    
    def test_there_are_students_and_teachers(self):
        teacher_1 = Teacher.objects.create(username = 'Teacher #1')
        student_1 = Student.objects.create(username = 'Student #1')
        self.assertEqual(Student.objects.all().count() + Teacher.objects.all().count() > 1, True)
    
    def test_the_teacher_can_teach_in_several_groups(self):
        teacher_1 = Teacher.objects.create(username = 'Teacher #1')
        group_1 = Group.objects.create()
        group_2 = Group.objects.create()
        teacher_1.groups.add(group_1, group_2)
        self.assertEqual(teacher_1.groups.all().count() > 1, True)
    
    def test_student_can_be_in_only_one_group(self):
        student_1 = Student.objects.create(username = 'Student #1')
        user_1 = User.objects.create(username = 'User #1')
        group_1 = Group.objects.create()
        group_2 = Group.objects.create()
        student_1.groups.add(group_1, group_2)
        #group_validate(student_1)
        #self.assertEqual(student_1.groups.all().count() == 0, True)
    
    def test_group_can_be_tied_to_several_сourses(self):
        teacher_1 = Teacher.objects.create(username = 'Teacher #1')
        group_1 = Group.objects.create()
        teacher_1.groups.add(group_1)
        course_1 = Course.objects.create()
        course_2 = Course.objects.create()
        practicecategory_1 = PracticeCategory.objects.create(course = course_1)
        practicecategory_2 = PracticeCategory.objects.create(course = course_2)
        practicetask_1 = PracticeTask.objects.create(category = practicecategory_1)
        practicetask_2 = PracticeTask.objects.create(category = practicecategory_2)
        userprogress_1 = UserProgress.objects.create(user = teacher_1, score = 0, practicetask = practicetask_1)
        userprogress_2 = UserProgress.objects.create(user = teacher_1, score = 0, practicetask = practicetask_2)
        self.assertEqual(userprogress_1.user == teacher_1 and teacher_1.groups.get() == group_1 and userprogress_1.practicetask == practicetask_1 and practicetask_1.category == practicecategory_1 and practicecategory_1.course == course_1, True)
        self.assertEqual(userprogress_2.user == teacher_1 and teacher_1.groups.get() == group_1 and userprogress_2.practicetask == practicetask_2 and practicetask_2.category == practicecategory_2 and practicecategory_2.course == course_2, True)

    def test_there_are_complaints(self):
        teacher_1 = Teacher.objects.create(username = 'Teacher #1')
        usercomplaints_1 = UserComplaint.objects.create(user = teacher_1, complaints = 'complaint #1')
        self.assertEqual(usercomplaints_1.complaints == 'complaint #1', True)

    def test_there_are_reviews(self):
        student_1 = Student.objects.create(username = 'Student #1')
        reviewsonteacher_1 = ReviewsOnTeacher.objects.create(student = student_1, reviews = 'review #1', fullname = 'Ivan')
        self.assertEqual(reviewsonteacher_1.reviews == 'review #1', True)

