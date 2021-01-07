from django.db import models

# Create your models here.

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
    gwizdki = models.IntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

