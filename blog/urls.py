from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create', views.create_blog_posts, name='create'),
    path('', views.blog_list, name='list'),
    path('post/<int:pk>/', views.blog_detail, name='detail'),
    path('test/', views.api_test, name='api_test'),
]

