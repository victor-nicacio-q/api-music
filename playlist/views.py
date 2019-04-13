from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

class Record_ViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = Record_Serializer
    #permission_classes = (permissions.IsAdminUser)

class Genre_ViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = Genre_Serializer
    #permission_classes = (permissions.IsAdminUser)

class Band_ViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = Band_Serializer
    permission_classes = (permissions.IsAdminUser)

class Music_ViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = Music_Serializer
    #permission_classes = (permissions.IsAdminUser)

class Playlist_ViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = Playlist_Serializer
    #permission_classes = (permissions.IsAdminUser)

##########
# CRUD COmpleto: list, create, retrieve, update, partial_update, destroy
#
# Sempre retornando a request nos overrides