from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from learning_system.users.views import student_api, teacher_api, user_api

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'study-groups', student_api.StudyGroupView)
router.register(r'students', student_api.StudentView)
router.register(r'teachers', teacher_api.TeacherView)
router.register(r'student_progress', student_api.StudentProgressView)
router.register(r'user_complaints', user_api.UserComplaintView)

urlpatterns = [
    url(r'login/$', user_api.UserLoginView.as_view(), name="login_user"),
    url(r'logout/$', user_api.UserLogoutView.as_view(), name="logout_user"),
    url('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('', include(router.urls))
]
