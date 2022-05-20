from atexit import register
from django.urls import path
from user.views import *

app_name = 'user'

urlpatterns = [
    path('list/', users, name ='user_list'),
    path('register/', user_register_form, name ='user_register_form'),
    path('create/', user_register, name ='user_register'),
    path('login/', user_login, name ='user_login'),



]