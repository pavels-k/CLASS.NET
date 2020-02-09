from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/v1/users/', include('learning_system.users.urls')),
    path('core/v1/', include('core.urls')),
]
