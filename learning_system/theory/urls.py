from django.conf.urls import url, include
from rest_framework import routers

from learning_system.theory import views

app_name = 'theory'
 
router = routers.DefaultRouter()
router.register(r'theory_category', views.TheoryCategoryView)    
router.register(r'theory_post', views.TheoryPostView)    

urlpatterns = [
    url('', include(router.urls))

]
