
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework.authtoken import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', views.obtain_auth_token)
    
]

