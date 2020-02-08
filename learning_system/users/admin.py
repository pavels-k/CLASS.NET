from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from learning_system.users.models import User, Student, Teacher, Group, UserProgress, UserComplaint, ReviewsOnTeacher


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(UserProgress)
admin.site.register(UserComplaint)
admin.site.register(ReviewsOnTeacher)

