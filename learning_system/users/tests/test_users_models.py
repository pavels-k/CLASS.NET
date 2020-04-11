from django.test import TestCase

from learning_system.courses.models import Course
from learning_system.practice.models import PracticeCategory
from learning_system.users.models import Student, Teacher, StudentProgress, UserComplaint, ReviewsOnTeacher, \
    StudyGroup, User

'''
class UserModelTest(TestCase):
    def test_student_create(self):
        group = StudyGroup.objects.create(name='group')
        Student.objects.create(username='student_1', study_group=group)
        self.assertEqual(Student.objects.exists(), True)

    def test_teacher_create(self):
        Teacher.objects.create(username='teacher_1')
        self.assertEqual(Teacher.objects.exists(), True)

    def test_the_teacher_can_teach_in_several_groups(self):
        teacher = Teacher.objects.create(username='teacher_1')
        group1 = StudyGroup.objects.create(name='group1')
        group2 = StudyGroup.objects.create(name='group2')
        teacher.study_groups.add(group1, group2)
        self.assertEqual(teacher.study_groups.count(), 2)

    def test_group_can_be_tied_to_several_сourses(self):
        group_1 = StudyGroup.objects.create()
        student_1 = Student.objects.create(username='Student #1', study_group=group_1)
        course_1 = Course.objects.create()
        course_2 = Course.objects.create()
        practicecategory_1 = PracticeCategory.objects.create(course=course_1)
        practicecategory_2 = PracticeCategory.objects.create(course=course_2)
        practicetask_1 = PracticeTask.objects.create(category=practicecategory_1)
        practicetask_2 = PracticeTask.objects.create(category=practicecategory_2)
        studentprogress_1 = StudentProgress.objects.create(student=student_1, score=0, practice_task=practicetask_1)
        studentprogress_2 = StudentProgress.objects.create(student=student_1, score=0, practice_task=practicetask_2)
        self.assertEqual(
            studentprogress_1.student == student_1 and student_1.study_group == group_1 and studentprogress_1.practice_task == practicetask_1 and practicetask_1.category == practicecategory_1 and practicecategory_1.course == course_1,
            True)
        self.assertEqual(
            studentprogress_2.student == student_1 and student_1.study_group == group_1 and studentprogress_2.practice_task == practicetask_2 and practicetask_2.category == practicecategory_2 and practicecategory_2.course == course_2,
            True)

    def test_there_are_complaints(self):
        teacher_1 = Teacher.objects.create(username='Teacher #1')
        usercomplaints_1 = UserComplaint.objects.create(user=teacher_1, complaints='complaint #1')
        self.assertEqual(usercomplaints_1.complaints == 'complaint #1', True)

    def test_there_are_reviews(self):
        group_1 = StudyGroup.objects.create()
        student_1 = Student.objects.create(username='Student #1', study_group=group_1)
        reviewsonteacher_1 = ReviewsOnTeacher.objects.create(student=student_1, reviews='review #1', fullname='Ivan')
        self.assertEqual(reviewsonteacher_1.reviews == 'review #1', True)

    def test_student_create1(self):
        group = StudyGroup.objects.create(name='group')
        student_1 = Student.objects.create(username='student_1', study_group=group)
        student_2 = Student.objects.create(username='student_2', study_group=group)
        students = Student.objects.filter(study_group=group)


        course_1 = Course.objects.create()
        course_2 = Course.objects.create()
        practicecategory_1 = PracticeCategory.objects.create(course=course_1)
        practicecategory_2 = PracticeCategory.objects.create(course=course_2)
        practicetask_1 = PracticeTask.objects.create(category=practicecategory_1)
        practicetask_2 = PracticeTask.objects.create(category=practicecategory_2)
        studentprogress_1 = StudentProgress.objects.create(student=student_1, score=0, practice_task=practicetask_1)
        studentprogress_2 = StudentProgress.objects.create(student=student_1, score=0, practice_task=practicetask_2)

        study_groups = StudentProgress.objects.filter(student = students)

        self.assertEqual(Student.objects.exists(), True)
'''