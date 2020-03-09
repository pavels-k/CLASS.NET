from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from learning_system.users.models import User, Student, Teacher, StudyGroup, StudentProgress, UserComplaint, ReviewsOnTeacher


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudyGroup)
admin.site.register(StudentProgress)
admin.site.register(UserComplaint)
admin.site.register(ReviewsOnTeacher)

