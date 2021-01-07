from django.contrib import admin
from .models import Film, ExtraInfo, Recenzja

class AdminFilm(admin.ModelAdmin):
    list_display = ('id', 'tytul','premiera','rok','imdb_rating')
    list_display_links = ('id','tytul')
    list_filter = ('id', 'tytul','premiera','rok')
    search_fields = ('id', 'tytul','premiera','rok')


admin.site.register(Film, AdminFilm)
admin.site.register(ExtraInfo)
admin.site.register(Recenzja)