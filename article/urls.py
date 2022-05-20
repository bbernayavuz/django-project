from django.urls import path
from article.views import *

app_name = 'article'

urlpatterns = [
    path('index/', article_index,name ='article_list'),
    path('new/', article_new_form, name ='article_new_form'),
    path('create/', article_create, name='article_create_url'),
    path('edit/<int:id>', article_edit, name='article_edit'),
    path('update/<int:id>', article_update, name='article_update_url'),
    path('delete/<int:id>', article_delete, name='article_delete_url'),

]