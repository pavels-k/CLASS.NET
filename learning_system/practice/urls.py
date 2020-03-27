from django.conf.urls import url, include
from rest_framework import routers

from learning_system.practice import views

app_name = 'practice'

router = routers.DefaultRouter()
router.register(r'practice_category', views.PracticeCategoryView)
router.register(r'practice_tasks', views.PracticeTaskView)
router.register(r'task_user_data', views.TaskUserDataView)

urlpatterns = [
    url('', include(router.urls))
]
