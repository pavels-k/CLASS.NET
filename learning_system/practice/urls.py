from django.conf.urls import url

from . import views

app_name = 'practice'

urlpatterns = [
    url(r'practice_category/create/$', views.PracticeCategoryCreateView.as_view(), name="create_practice_category"),
    url(r'practice_task/create/$', views.PracticeTaskCreateView.as_view(), name="create_practice_task"),
    url(r'task_user_data/create/$', views.TaskUserDataCreateView.as_view(), name="create_task_user_data"),

    url(r'practice_category/list$', views.PracticeCategoryView.as_view(), name="practice_category_list"),
    url(r'practice_task/list$', views.PracticeTaskView.as_view(), name="practice_task_list"),
    url(r'task_user_data/list$', views.TaskUserDataView.as_view(), name="task_user_data_list"),
    url(r'practice_task/update/(?P<pk>\d+)$', views.PracticeTaskUpdateDeleteView.as_view(), name="practice_task_update"),
    #url(r'practice_task/student/list$', views.GetPracticeForStudents.as_view(), name="practice_task_student_list"),    
    url(r'get_task_list_for_student$', views.GetTaskListView.as_view(), name='get_task_list_for_student')
]
# GetPracticeForStudents