from django.conf.urls import url, include
from rest_framework import routers

from learning_system.users import views

app_name = 'users'

router = routers.DefaultRouter()
#router.register(r'student_move', views.StudentViewSet)
#router.register(r'get/results/studygroup/', views.GroupSelectView)    
#router.register(r'get/results/students', views.StudentSelectView)    

urlpatterns = [
    url(r'group/create/$', views.StudyGroupCreateView.as_view(), name="create_group"),
    url(r'student/create/$', views.StudentCreateView.as_view(), name="create_student"),
    url(r'teacher/create/$', views.TeacherCreateView.as_view(), name="create_teacher"),
    url(r'login/$', views.UserLoginView.as_view(), name="login_user"),
    url(r'logout/$', views.UserLogoutView.as_view(), name="logout_user"),
    url(r'student_progress/create/$', views.StudentProgressCreateView.as_view(), name="create_student_progress"),
    url(r'user_complaint/create/$', views.UserComplaintCreateView.as_view(), name="create_user_complaint"),
    url(r'reviews_on_teacher/create/$', views.ReviewsOnTeacherCreateView.as_view(), name="create_reviews_on_teacher"),

    url(r'group/list$', views.StudyGroupView.as_view(), name="group_list"),
    url(r'student/list$', views.StudentView.as_view(), name="student_list"),
    url(r'teacher/list$', views.TeacherView.as_view(), name="teacher_list"),
    url(r'student_progress/list$', views.StudentProgressView.as_view(), name="student_progress_list"),
    url(r'user_complaint/list$', views.UserComplaintView.as_view(), name="user_complaint_list"),
    url(r'reviews_on_teacher/list$', views.ReviewsOnTeacherView.as_view(), name="reviews_on_teacher_list"),
    url(r'get_task_list_for_student$', views.GetTaskListView.as_view(), name='get_task_list_for_student'),    
    url(r'set_group_for_student/(?P<pk>\d+)$', views.SetGroupView.as_view(), name="set_group_for_student"),
    url(r'add_study_group_to_course/(?P<pk>\d+)$', views.AddCourseToStudyGroupView.as_view(), name='add_study_group_to_course'),    
    url(r'get/results/study_group/(?P<pk>\d+)$', views.GroupSelectView.as_view(), name='Study_Group_Result_List'),    
    url(r'students/get_progress/$', views.StudentResultList.as_view(), name='Student_Result_List'),    
    url('', include(router.urls))
]
#StudentResultList