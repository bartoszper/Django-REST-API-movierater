from django.contrib import admin
from .models import Film, ExtraInfo, Recenzja, Aktor

class AdminFilm(admin.ModelAdmin):
    list_display = ('id', 'tytul','premiera','rok','imdb_rating')
    list_display_links = ('id','tytul')
    list_filter = ('id', 'tytul','premiera','rok')
    search_fields = ('id', 'tytul','premiera','rok')

class AktorAdmin(admin.ModelAdmin):
    list_display = ('imie','nazwisko')
    list_display_links = ('imie','nazwisko')
    list_filter = ('imie','nazwisko')
    search_fields = ('imie','nazwisko')


admin.site.register(Film, AdminFilm)
admin.site.register(ExtraInfo)
admin.site.register(Recenzja)
admin.site.register(Aktor, AktorAdmin)