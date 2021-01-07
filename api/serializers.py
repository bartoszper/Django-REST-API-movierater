from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id','tytul', 'opis', 'po_premierze', 'premiera','rok','imdb_rating']


