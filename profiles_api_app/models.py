# createsuperuser details--> email=kj@gmail.com,name=kushal, password=pass1234


from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
# the AbstractBaseUser is the base of the django's standard user model
# we are going to override the default user model that django provides us with our own customized user model
from django.contrib.auth.models import PermissionsMixin
# to include all the permissions for our customized user model that the base model would otherwise have
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Helps django work with our custom user model """

    def create_user(self,email,name,password=None):
        """ creates a new user profile object. """

        if not email:  # checks whether  email field  has been filled
            raise ValueError('Users must have a valid email address')

        email=self.normalize_email(email) # normalizes ~> converts all chars to lowercase to maintain uniformity

        user=self.model(email=email,name=name)#creates a new user object for the custom profile we have made
        # self.model implies the model it is linked to , which in this case is UserProfile model
        # the link in the connection is ~>BaseUserManager->AbstractBaseUser(UserProfile model)

        user.set_password(password) # converts password to #####
        user.save(using=self.db) # saves in database

        return user

    def create_superuser(self,name,email,password):
        """ creates and saves a new superuser(admin privileges) with given details ."""

        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True

        user.save(using=self.db)

        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    # Represents a user profile in our system

    email=models.EmailField(max_length=120,unique=True)
    name=models.CharField(max_length=120)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager() # helps in managing the user profiles and gives us some extra functionality like
                                 # creating an admin user or a regular user.
                                 # moreover it's required when we are overwriting the base user model

    USERNAME_FIELD='email' # the standarddjango model has a field called USERNAME_FIELD which acts as the username or
                           # a handle which is used to login etc.We have set that field to email instead of a custom username.

    REQUIRED_FIELDS=['name'] # fields that the user must fill in to register

    def get_full_name(self):
        """ used to get a user's full name."""

        return self.name

    def get_short_name(self):
        """ used to get user's short name """

        return self.name

    def __str__(self):
        """ django uses this when it needs to convert the object to a string """
        return self.email

class ProfileFeedItem(models.Model):
    """ Profile status update."""

    user_profile=models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    # on_delete tells django/database what to do if the UserProfile to which the feed is linked to (via ForeignKey) itslef gets deleted
    # i.e CASCADE tells db that if the user deletes his own profile then go on delete all his status updates,feeds etc.

    status_text=models.CharField(max_length=100) # String of status a user puts on display to describe his profile
    created_on=models.DateTimeField(auto_now_add=True) # Field for storing dates and times
    # @param auto_now_add -->Basically says automatically set the time to now if we don't specify a time when we create an object.


    def __str__(self):
        """ Return model as a string. """
        return self.status_text
