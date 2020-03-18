
from django.conf.urls import url

from learning_system.courses import views

app_name = 'courses'

urlpatterns = [
    url(r'course/create/$', views.CourseCreateView.as_view(), name="create_course"),
    url(r'course/list$', views.CourseView.as_view(), name="course_list"),
]
