from django.urls import path
from .views import login_app, register, exit

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    path('login/', login_app, name='index')
]