from django.conf.urls import url

from . import views

app_name = 'theory'

urlpatterns = [
    url(r'theory_category/create/$', views.TheoryCategoryCreateView.as_view(), name="create_theory_category"),
    url(r'theory_post/create/$', views.TheoryPostCreateView.as_view(), name="create_theory_post"),
    url(r'theory_category/list$', views.TheoryCategoryView.as_view(), name="theory_category_list"),
    url(r'theory_post/list$', views.TheoryPostView.as_view(), name="theory_post_list"),
]
