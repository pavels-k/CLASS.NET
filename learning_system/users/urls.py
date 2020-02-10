from django.contrib import admin
from django.urls import path, include
from learning_system.users.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'learnig_system'
urlpatterns = [
    path('group/create', GroupCreateView.as_view()),
    path('user/create', CreateUserView.as_view()),
    #path('user/set', UserViewSet.as_view())
]


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', StudentViewSet, basename='MyModel')

# The API URLs are now determined automatically by the router.
urlpatterns += [
    path('set', include(router.urls)),
]