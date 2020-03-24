from django.conf.urls import url, include
from rest_framework import routers

from learning_system.users.views import student_api, teacher_api, user_api

app_name = 'users'

router = routers.DefaultRouter()
#router.register(r'groupss', student_api.StudyGroupView)
router.register(r'group', student_api.StudyGroupCreateView)    
router.register(r'students', student_api.StudentCreateView)    
router.register(r'teacher', teacher_api.TeacherCreateView)    
router.register(r'studentsss_progress', student_api.StudentProgressCreateView)    
router.register(r'user_complaint', user_api.UserComplaintCreateView)    
#router.register(r'student/list', student_api.StudentView)    
#router.register(r'teacher/list', teacher_api.TeacherView)    
#router.register(r'student_progress/list', student_api.StudentProgressView)    
#router.register(r'user_complaint/list', user_api.UserComplaintView)    
#router.register(r'reviews_on_teacher/list', student_api.ReviewsOnTeacherView)    
router.register(r'get_task_list_for_student', student_api.GetTaskListView)    
router.register(r'set_group_for_student', teacher_api.SetGroupView)    
router.register(r'add_study_group_to_course', user_api.StudyGroupView)    
#router.register(r'get/results/study_group', teacher_api.GroupSelectView)    
#router.register(r'students/get_progress', teacher_api.StudentResultList)    

urlpatterns = [
    #url(r'group/create/$', student_api.StudyGroupCreateView.as_view(), name="create_group"),
    #url(r'student/create/$', student_api.StudentCreateView.as_view(), name="create_student"),
    #url(r'teacher/create/$', teacher_api.TeacherCreateView.as_view(), name="create_teacher"),
    url(r'login/$', user_api.UserLoginView.as_view(), name="login_user"),
    url(r'logout/$', user_api.UserLogoutView.as_view(), name="logout_user"),
    #url(r'student_progress/create/$', student_api.StudentProgressCreateView.as_view(), name="create_student_progress"),
    #url(r'user_complaint/create/$', user_api.UserComplaintCreateView.as_view(), name="create_user_complaint"),
    #url(r'reviews_on_teacher/create/$', student_api.ReviewsOnTeacherCreateView.as_view(), name="create_reviews_on_teacher"),


    #url(r'group/list$', student_api.StudyGroupView.as_view(), name="group_list"),
    #url(r'student/list$', student_api.StudentView.as_view(), name="student_list"),
    #url(r'teacher/list$', teacher_api.TeacherView.as_view(), name="teacher_list"),
    #url(r'student_progress/list$', student_api.StudentProgressView.as_view(), name="student_progress_list"),
    #url(r'user_complaint/list$', user_api.UserComplaintView.as_view(), name="user_complaint_list"),
    #url(r'reviews_on_teacher/list$', student_api.ReviewsOnTeacherView.as_view(), name="reviews_on_teacher_list"),
    #url(r'get_task_list_for_student$', student_api.GetTaskListView.as_view(), name='get_task_list_for_student'),    
    #url(r'set_group_for_student/(?P<pk>\d+)$', teacher_api.SetGroupView.as_view(), name="set_group_for_student"),
    #url(r'add_study_group_to_course/(?P<pk>\d+)$', user_api.AddCourseToStudyGroupView.as_view(), name='add_study_group_to_course'),    
    url(r'get/results/study_group/(?P<pk>\d+)$', teacher_api.GroupSelectView.as_view(), name='Study_Group_Result_List'),    
    url(r'students/get_progress/$', teacher_api.StudentResultList.as_view(), name='Student_Result_List'),    
    url('', include(router.urls))
]
