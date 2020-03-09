from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/v1/users/', include('learning_system.users.urls')),
    path('core/v1/practice/', include('learning_system.practice.urls')),
    path('core/v1/courses/', include('learning_system.courses.urls')),
    path('core/v1/theory/', include('learning_system.theory.urls')),
]
