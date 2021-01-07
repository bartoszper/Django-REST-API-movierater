
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'filmy', views.FilmViewSet)
router.register(r'recenzje', views.RecenzjaViewSet)



urlpatterns = [
    path('', include(router.urls)),
   
]
