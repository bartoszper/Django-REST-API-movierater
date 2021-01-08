from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.

@receiver(post_save, Sender = User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ExtraInfo(models.Model):
    RODZAJE = {
        (0, 'Nieznany'),
        (1, 'Horror'),
        (2, 'Sci-Fi'),
        (3, 'Dramat'),
        (5, 'Komedia'),
    }

    czas_trwania = models.IntegerField()
    rodzaj = models.IntegerField(choices=RODZAJE, default=0)
class Film(models.Model):
    tytul = models.CharField(max_length=50)
    opis = models.TextField()
    po_premierze = models.BooleanField(default=False)
    premiera = models.DateField(null=True, blank=True)
    rok = models.IntegerField()
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=4 ,blank=True, null=True)
    extra_info = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul

class Recenzja(models.Model):
    opis = models.TextField(default='')
    gwiazdki = models.IntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='recenzje')

class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)

    def __str__(self):
        return imie
