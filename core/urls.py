from django.urls import include, path

urlpatterns = [
    #path('learning_system/users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]