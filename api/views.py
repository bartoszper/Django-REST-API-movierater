from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from .serializers import UserSerializer
from .models import Film, Recenzja, Aktor
from .serializers import FilmSerializer, RecenzjaSerializer, AktorSerializer
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class FilmyResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3


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
    
    serializer_class = FilmSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['tytul', 'opis','rok']
    search_fields = ('tytul','opis')
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    pagination_class = FilmyResultsSetPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # rok = self.request.query_params.get('rok',None)
        # if rok:
        #     filmy = Film.objects.filter(rok=rok)
        # else:
        filmy = Film.objects.all()
        return filmy


    def create(self, request, *args, **kwargs):
        #if request.user.is_staff:
        film = Film.objects.create(tytul=request.data['tytul'], opis=request.data['opis'], po_premierze=request.data['po_premierze'],rok =request.data['rok'])
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)
        #else:
        #   return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.tytul = request.data['tytul']
        film.opis = request.data['opis']
        film.rok = request.data['rok']
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


class RecenzjaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recenzja.objects.all()
    serializer_class = RecenzjaSerializer

class AktorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer

    @action(detail=True, methods=['POST'])
    def add_film(self, request, **kwargs):
        aktor = self.get_object()
        film = Film.objects.get(id=request.data['film'])
        aktor.filmy.add(film)

        serializer = AktorSerializer(aktor, many=False)
        return Response(serializer.data)



