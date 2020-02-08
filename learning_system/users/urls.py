from django.contrib import admin
from django.urls import path, include
from learning_system.users.views import *

app_name = 'learnig_system'
urlpatterns = [
    path('user/create', UserCreateView.as_view())
]