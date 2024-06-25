from django.urls import path, include
from .views import *

urlpatterns = [
    # Para las tarjetas de crédito
    path('cards/', get_creditcards, name='CREDIT CARDS'),
    path('cards/add/', create_creditcard, name='ADD CREDIT CARD'),
    path('cards/<str:pk>/', update_creditcard, name='MANAGE CREDIT CARD'),
    path('cards/<str:pk>/delete/', delete_creditcard, name='DELETE CREDIT CARD'),
    
    # Para las compras
    path('purchases/', get_purchases, name='PURCHASES'),
    path('purchases/add/', create_purchase, name='ADD PURCHASE'),
    path('purchases/<str:pk>/', get_purchase, name='MANAGE PURCHASE'),
    path('purchases/<str:pk>/update/', update_purchase, name='UPDATE PURCHASE'),
]