#from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializer

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format = None):
        """Returns A List of API View Features"""
        an_apiview = [
        'uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives You the most control over you application logic',
        'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview })

    def post(self, request):
        """Create a Hello Message with One Name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handling  Updating an Object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    def list(self, request):
        """Return Hello Message"""

        a_viewset =['uses actions (list, create, Retrieve, update, partial_update)',
        'automatically maps URLs using Routers ',
        'Provides less functionality with less code',]
