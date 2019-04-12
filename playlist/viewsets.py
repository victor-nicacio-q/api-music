from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class Record_ViewSet(ModelViewSet):

    queryset = Record.objects.all()
    serializer_class = Record_Serializer

class Genre_ViewSet(ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = Genre_Serializer

class Band_ViewSet(ModelViewSet):

    queryset = Band.objects.all()
    serializer_class = Band_Serializer

class Music_ViewSet(ModelViewSet):

    queryset = Music.objects.all()
    serializer_class = Music_Serializer

class Playlist_ViewSet(ModelViewSet):

    queryset = Playlist.objects.all()
    serializer_class = Playlist_Serializer