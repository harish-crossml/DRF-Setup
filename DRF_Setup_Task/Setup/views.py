from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HomeSerializer
from .models import *


class HomeView(APIView):
    def get(self, request):
        queryset = Home.objects.all()
        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request, pk):
        home = Home.objects.get(pk=pk)
        serializer = HomeSerializer(home, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        home = Home.objects.get(pk=pk)
        home.delete()
        return Response({'success': 'deleted successfully'})

class HomeDetailView(APIView):
    def get(self, request, pk):
        try:
            home = Home.objects.get(pk=pk)
        except Home.DoesNotExist:
            return Response({'error': 'Home does not exist'}, status=404)
        serializer = HomeSerializer(home)
        return Response(serializer.data)


