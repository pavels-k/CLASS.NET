
from rest_framework import permissions
from .models import Student

class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated: 
            return request.user.role == 'S' 
        return False

class IsTeacherOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            is_teacher = (request.user.role == 'T') 
            return bool(is_teacher | request.user.is_staff)
        return False