from django.db import models

# Create your models here.

class Film(models.Model):
    tytul = models.CharField(max_length=50)
    opis = models.TextField()
    po_premierze = models.BooleanField(default=False)
    
