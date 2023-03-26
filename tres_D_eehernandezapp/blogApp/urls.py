from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('posts/', posts, name='posts'),
    path('search/', search, name='search'),
    path('posts/create/', create_post, name='create_posts'),
    path('tag/create/', create_tag, name='create_tag'),
    path('categoria/create/', create_categoria, name='create_categoria'),
    path('posts/<int:id>/', edit_post, name='edit_post'),
    path('posts/<int:id>/delete/', delete_post, name='delete_post')
]