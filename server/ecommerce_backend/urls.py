from django.contrib import admin
from django.urls import path, include
from app_users import urls as urls_users
from app_users.views import MyTokenObtainPairView
from app_products import urls as urls_products
from app_checkout import urls as urls_checkout
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include(urls_users)),
    path('api/products/', include(urls_products)),
    path('api/checkout/', include(urls_checkout)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='OBTENCIÓN DE TOKEN'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='ACTUALIZACIÓN DE TOKEN'),
]
