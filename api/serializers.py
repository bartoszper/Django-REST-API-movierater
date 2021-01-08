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
        fields = ('id','opis','gwiazdki','film')

    def create(self, instance, validated_data):
        instance.opis = validated_data.get('opis', instance.opis)
        instance.gwiazdki = validated_data.get('gwiazki', instance.gwiazdki)
        instance.save()

        return instance

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    recenzje = RecenzjaSerializer(many=True)
    class Meta:
        model = Film
        fields = ['id','tytul', 'opis', 'po_premierze', 'premiera','rok','imdb_rating','extra_info','recenzje']
        read_only_fields = ('extra_info','recenzje')

class AktorSerializer(serializers.HyperlinkedModelSerializer):
    filmy = FilmSerializer(many=True, read_only=True)
    class Meta:
        model = Aktor
        fields = ['id','imie','nazwisko','filmy']
    
    # def create(self, validated_data):
    #     filmy = validated_data['filmy']
    #     del validated_data['filmy']

    #     aktor = Aktor.objects.create(**validated_data)

    #     for film in filmy:
    #         f = Film.objects.create(**film)
    #         aktor.filmy.add(f)
    #     aktor.save()
    #     return aktor



