from django.shortcuts import render

# Create your views here.
# api views take care of the code that is ran when the user visits our api endpoint.

from rest_framework.views import APIView
from rest_framework.response import Response#Response object is the standard response object that we
# return from our APIView that can be rendered  into an Api o/p

from . import serializers # . implies current/root directory

from rest_framework import status # list of various http response status codes like http 404,200,505 etc.
# all these codes are described in the status module of rest_framework.

class HelloApiView(APIView):
    """ Test api view. """
    # APIViews work by defining functions that match the standard HTTP methods like GET,POST etc

    serializer_class=serializers.HelloSerializer # this tells django the serializer class for this APIView
    # will be the HelloSerializer class

    def get(self,request,format=None):
        """ Returns a list of API view features .Here we are going to create a manual list of objects and
        return it ."""

        an_apiview=[
        'Uses HTTP methods as functions(get,post ,put,delete )',
        'It is similar to a traditional Django view ',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',
        ]
        # A Response must be a part of a dictionary .
        # A response is effectively a dictionary which is converted into json and then output to the screen
        return Response({'message':'Hello','an_apiview':an_apiview});


    def post(self,request):
        """ Create a hello message with our name . """
        # when you make a post request to our api view , we are going to return a message that includes the NAME
        # that was posted to the Api

        serializer=serializers.HelloSerializer(data=request.data) # serializer is an instance of HelloSerializer

        if serializer.is_valid():  # checks if the entry (post request) is valid (validators are those we used in serializers.py file like max_length etc)
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """ Handles updation of an object. """
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """ Patch request,only updates fields provided in the request."""
        return Response({'method':'patch'})


    def delete(self,request,pk=None):
        """ Deletes an object"""
        return Response({'method':'delete'})
