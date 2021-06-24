from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # path('b/', views.blog, name='blog_b'),
    path('detail/', views.detail_view, name='detail_view'),

    path('search/', views.api_search_data, name='search'),
    path('blog/', views.blog, name='blog'),
    # path('git/', views.github_user_login, name='gitdeatil'),

    path('github/', views.github_user_login, name='github'),

]
# validate_username
