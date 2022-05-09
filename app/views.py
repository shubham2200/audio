from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from .serilaizer import *
from rest_framework.generics import ListAPIView
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics



# Create your views here.

class PostSongs(APIView):
    def post(self, request ,format=None):
        seri =   SongSerializer(data = request.data)
        if seri.is_valid():
            seri.save()
            # data = {'seri':data.data}
            print(seri.data,'daata   ')
            return Response( seri.data,status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        items = Songs.objects.all()
        data = SongSerializer(items ,  many=True )
        i_data = data.data
        return Response(i_data ,status=status.HTTP_200_OK)

class UpdateDeleteSong(APIView):
    def put(self, request,pk):
        id = Songs.objects.get(pk=pk)
        print(id,'id')
        data = SongSerializer(instance=id, data=request.data)
        if data.is_valid():
            data.save()
            print(data.data,'hdhjdj')
            return Response(data.data ,status=status.HTTP_200_OK )  
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk):
        id = Songs.objects.get(pk=pk)
        print(id,'id')
        # data = SongSerializer(instance=id)
        id.delete()
        return Response('song has been delete  ',status=status.HTTP_200_OK ) 

class SongSearchListAPIView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['song_name','id']



