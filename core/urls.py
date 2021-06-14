from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # path('b/', views.blog, name='blog_b'),
    path('detail/',views.detail_view,name='detail_view'),

    path('search/', views.api_search, name='search'),
    path('blog/', views.blog, name='blog'),

    path('github/', views.get_github_data, name='github'),
    # path('search/<name>/', ArticleDetailView.as_view(), name='article-detail'),

]
# validate_username
