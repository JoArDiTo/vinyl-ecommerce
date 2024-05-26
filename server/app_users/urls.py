from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_users, name='USERS'),
    path('add/', add_user, name='ADD USER'),
    path('<str:pk>/',get_user, name='MANAGE USER'),
    path('<str:pk>/update/', update_user, name='UPDATE USER'),
    path('<str:pk>/update/password/', update_password, name='UPDATE PASSWORD'),
    path('<str:pk>/delete/', delete_user, name='DELETE USER')
]