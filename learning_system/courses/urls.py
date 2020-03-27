from django.conf.urls import url, include
from rest_framework import routers

from learning_system.courses import views

app_name = 'courses'

router = routers.DefaultRouter()
router.register(r'course', views.CourseView)

urlpatterns = [url('', include(router.urls))]
