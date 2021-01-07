from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film, ExtraInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class ExtraInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwania','rodzaj']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    class Meta:
        model = Film
        fields = ['id','tytul', 'opis', 'po_premierze', 'premiera','rok','imdb_rating','extra_info']


