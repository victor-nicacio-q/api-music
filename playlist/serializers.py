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

    class Meta:
        model = Band
        fields = '__all__'

class Music_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

class Playlist_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'