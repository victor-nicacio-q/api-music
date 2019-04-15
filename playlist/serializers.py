from rest_framework import serializers
from .models import *

class Record_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'

class Genre_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class Band_Serializer(serializers.ModelSerializer):

    genre = Genre_Serializer(many=False)
    record = Record_Serializer(many=False)

    class Meta:
        model = Band
        fields = (
            'name',
            'genre',
            'record'
        )

class Music_Serializer(serializers.ModelSerializer):

    band = Band_Serializer(many=False)

    class Meta:
        model = Music
        fields = (
            'name',
            'band',
            'duration',
            'year'
        )

class Playlist_Serializer(serializers.ModelSerializer):

    music = Music_Serializer(many=True)
    class Meta:
        model = Playlist
        fields = (
            'name',
            'music'
        )