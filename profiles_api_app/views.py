from django.shortcuts import render

# Create your views here.
# api views take care of the code that is ran when the user visits our api endpoint.
from rest_framework.views import APIView
from rest_framework.response import Response
 #Response object is the standard response object that we return from our APIView that can be rendered  into an Api o/p

class HelloApiView(APIView):
    """ Test api view. """
    # APIViews work by defining functions that match the standard HTTP methods like GET,POST etc
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
