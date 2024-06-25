from django.urls import path, include
from .views import *

urlpatterns = [
    # Para los vinilos
    path('vinyls/', get_products, name='PRODUCTS'),
    path('vinyls/add/', add_product, name='ADD PRODUCT'),
    path('vinyls/<str:pk>/', get_product, name='MANAGE PRODUCT'),
    path('vinyls/<str:pk>/update/', update_product, name='UPDATE PRODUCT'),
    path('vinyls/<str:pk>/delete/', delete_product, name='DELETE PRODUCT'),
    
    # Para las canciones que tiene los vinilos
    path('songs/', get_songs, name='SONGS'),
    path('songs/add/', add_song, name='ADD SONG'),
    path('songs/<str:pk>/', get_song, name='MANAGE SONG'),
    path('songs/<str:pk>/update/', update_song, name='UPDATE SONG'),
    path('songs/<str:pk>/delete/', delete_song, name='DELETE SONG'),
    
    # Para las categorias
    path('categories/', get_categories, name='CATEGORIES'),
    path('categories/add/', add_category, name='ADD CATEGORY'),
    path('categories/<str:pk>/', get_category, name='MANAGE CATEGORY'),
    path('categories/<str:pk>/update/', update_category, name='UPDATE CATEGORY'),
    path('categories/<str:pk>/delete/', delete_category, name='DELETE CATEGORY'),
    
    # Para las relaciones entre vinilos y categorias
    path('vinyls-categories/', get_vinyl_categories, name='VINYL CATEGORIES'),
    path('vinyls-categories/add/', add_vinyl_category, name='ADD VINYL CATEGORY'),
    path('vinyls-categories/<str:pk>/', get_vinyl_category, name='MANAGE VINYL CATEGORY'),
    path('vinyls-categories/<str:pk>/update/', update_vinyl_category, name='UPDATE VINYL CATEGORY'),    
    path('vinyls-categories/<str:pk>/delete/', delete_vinyl_category, name='DELETE VINYL CATEGORY')
]
