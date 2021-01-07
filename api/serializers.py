from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film, ExtraInfo, Recenzja, Aktor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class ExtraInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwania','rodzaj']


class RecenzjaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recenzja
        fields = ['opis','gwiazdki']


class AktorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aktor
        fields = ['imie','nazwisko','filmy']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    recenzje = RecenzjaSerializer(many=True)
    class Meta:
        model = Film
        fields = ['id','tytul', 'opis', 'po_premierze', 'premiera','rok','imdb_rating','extra_info','recenzje']




