from django.shortcuts import render



from rest_framework.views import APIView # api views take care of the code that is ran when
 #   the user visits our api endpoint.

from rest_framework.response import Response #Response object is the standard response object that we
# return from our APIView that can be rendered  into an Api o/p

from rest_framework import status # list of various http response status codes like http 404,200,505 etc.
# all these codes are described in the status module of rest_framework.

from rest_framework.authentication import TokenAuthentication  # most popular way of authentication in django. It works by giving
# the user a temporary token that it inserts in the headers of the http request . DRF can then use this token
# to check and verify if the user has authenticated with the system.

from rest_framework import viewsets

from rest_framework import filters # to search for entries in our api

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken # its an APIView used to create login functionalityin the Api


from . import serializers # . implies current/root directory
from . import models
from . import permissions



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



class HelloViewSet(viewsets.ViewSet):
    """ Test api ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Return a hello object. """

        a_viewset=[
        'Uses actions (list,create,retrieve,update,partial_update)',
        'Automatically maps to urls using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self,request):
        """ creates a new hello message. """

        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk=None):
        """Handles retrieval of an object by its id"""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Updates a part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Deletes an object """
        return Response({'http_method':'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating,reading and updating user profiles"""
    # the ModelViewSet is a special viewset in the rest_framework that taakes care of all of the logic
    # for creating,reading and updating our model items

    serializer_class=serializers.UserProfileSerializer

    queryset=models.UserProfile.objects.all() #returns a list of all the objects(UserProfile model) in our db
     # tells the viewset how to retrieve the objects from our database

    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)  # feature to search fields by name and email
    search_fields=('name','email')


class LoginViewSet(viewsets.ViewSet):
    """checks email and password and returns an auth token. """

    serializer_class=AuthTokenSerializer

    def create(self,request):# create function is called when a http post request is made to the ViewSet
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating , reading  and updating profile feed items."""

    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()


    def perform_create(self,serializer):
        """ sets the user profile to the currently logged-in user. """

        serializer.save(user_profile=self.request.user)
        
