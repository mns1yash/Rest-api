#from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Returns A List of API View Features"""
        an_apiview = [
        'uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives You the most control over you application logic',
        'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview })
