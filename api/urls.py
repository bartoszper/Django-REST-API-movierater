
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'filmy', views.FilmViewSet, basename='film')
router.register(r'recenzje', views.RecenzjaViewSet, basename='recenzje')
router.register(r'aktorzy', views.AktorViewSet, basename='aktorzy')



urlpatterns = [
    path('', include(router.urls)),
   
]
