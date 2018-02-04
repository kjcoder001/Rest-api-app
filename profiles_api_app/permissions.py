# A file to store all the permissions classes
# A permission class is a class that the rest_framework uses to determine if the user has the permission to make the
# change they're asking.

from rest_framework import permissions # this module contains all the base permission classes of django

class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit their own profile. """
# The way a permission class works is that the class has a function inside the class called "has_object_permission".
# This function is called every time a request is made to our api.The result of the function determines whether the
# user has the permission to perform the action.

    def has_object_permission(self,request,view,obj):
        """check user is trying to update their own profile."""


        if request.method in permissions.SAFE_METHODS:
            return True
# A user can "view" any profile they wish to but can edit only theirs. Certain methods in HTTP give only the content
# or read access to the request made ,e.g the GET method .Get method doesnt't change any data in the api/db.The
# permissions.SAFE_METHODS is list of such methods.

        return obj.id==request.user.id
# obj.id is the id of the profile the user wants to make changes to.It can only make this change if this id is same
# as the user making this request; since only a user can edit his own profile.!
