from rest_framework import viewsets, response, status
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

class Record_ViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Record.objects.all()

    serializer_class = Record_Serializer

    @api_view(['GET', 'POST'])
    def Record_list(self, request):
        if request.method == 'GET':
            records = Record.objects.all()
            serializer_class = Record_Serializer(records)
            return response.Response(serializer_class.data)
        elif request.method == 'POST':
            serializer_class = Record_Serializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return response.Response(serializer_class.data, status=status.HTTP_200_OK)
            return response.Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def Record_detail(self, request, pk ):

        try:
            record = Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer_class = Record_Serializer(record)
            return response.Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer_class = Record_Serializer(record, data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return response.Response(serializer_class.data, status=status.HTTP_200_OK)
            return response.Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            record.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)


class Genre_ViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Genre.objects.all()

    serializer_class = Genre_Serializer

    @api_view(['GET', 'POST'])
    def Genre_list(self, request):
        if request.method == 'GET':
            records = Record.objects.all()
            serializer_class = Genre_Serializer(records)
            return response.Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer_class = Genre_Serializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return response.Response(serializer_class.data, status=status.HTTP_200_OK)
            return response.Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def Genre_detail(self, request, pk):
        try:
            genre = Genre.object.get(pk=pk)
        except Genre.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer_class = Genre_Serializer(genre)
            return response.Response(serializer_class.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer_class = Genre_Serializer(genre, data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return response.Response(serializer_class.data, status=status.HTTP_200_OK)
            return response.Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            genre.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

class Band_ViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = Band_Serializer

class Music_ViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = Music_Serializer

class Playlist_ViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = Playlist_Serializer

'''
    CRUD - Create Read Update Delete
        list X
        update X
        retrieve X
        partial_update X
        destroy X
        create X
'''