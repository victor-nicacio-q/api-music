from django.contrib import admin
from .models import Record, Genre, Band, Music, Playlist

admin.site.register(Record)
admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Music)
admin.site.register(Playlist)
