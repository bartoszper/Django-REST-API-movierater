from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Film
from .serializers import FilmSerializer
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    

class FilmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def create(self, request, *args, **kwargs):
        #if request.user.is_staff:
        film = Film.objects.create(tytul=request.data['tytul'], opis=request.data['opis'], po_premierze=request.data['po_premierze'])
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)
        #else:
        #   return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.tytul = request.data['tytul']
        film.opis = request.data['opis']
        film.po_premierze = request.data['po_premierze']
        film.save()
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    
    def destroy(self, request, *args, **kwargs):
        film = self.get_object()
        film.delete()
        return Response('Film został usnięty')

    #My own method

    @action(detail=True)
    def premiera(self, request, **kwargs):
        film = self.get_object()
        film.po_premierze = True
        film.save()
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)


    @action(detail=False)
    def premiera_all(self, request, **kwargs):
        filmy = Film.objects.all()
        filmy.update(po_premierze = True)
    
        serializer = FilmSerializer(filmy, many=True)
        return Response(serializer.data)


    @action(detail=False)
    def przed_premiera_all(self, request, **kwargs):
        filmy = Film.objects.all()
        filmy.update(po_premierze = False)
    
        serializer = FilmSerializer(filmy, many=True)
        return Response(serializer.data)






