
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:id>/edit/', views.post_update, name='post_update'),
    path('<int:id>/delete/', views.post_delete, name='post_delete'),
]