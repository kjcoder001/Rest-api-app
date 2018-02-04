
""" A Serializer object is an object in the rest_framework that we can use to describe the data that
we need to return and retrieve from our api.Basically it converts text string of json to a python object and
vice-versa. """
from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView. """

    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects"""

    class Meta:
        model=models.UserProfile # tells django that ModelSerializer is going to be used with the UserProfile model
        fields=('id','email','name','password') # fields in the model that the serializer should use
        extra_kwargs={'password':{'write_only':True}} # extra keyword arguments ,allows us to associate certain extra
        # attributes and apply them to oue fields

        def create(self,validated_data): # validated_data holds the values the user provides after validation
            """Create and return a new user """

            user=models.UserProfile(email=validated_data['email'],name=validated_data['name'])
            user.set_password(validated_data['password']) # to convert the text string of password into a hash Value
            # so that profile passwords are securely stored in the database and not as raw string given by the user
            user.save()

            return user
