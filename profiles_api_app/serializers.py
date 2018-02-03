
""" A Serializer object is an object in the rest_framework that we can use to describe the data that
we need to return and retrieve from our api.Basically it converts text string of json to a python object and
vice-versa. """
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView. """

    name=serializers.CharField(max_length=10)
    
