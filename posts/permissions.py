from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    A custom permission class to allow read-only access to all authenticated
    users and write access to the author of the post only.
    """

    def has_permission(self, request, view):
        """
        Check if the request user is authenticated and has permission
        to access the API view.

        :param request: The request object.
        :param view: The view object.
        :return: True if the request user is authenticated and has permission,
            False otherwise.
        :rtype: bool
        """

        # Only authenticated users have API access
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Check if the request user is authenticated and has permission
        to perform write actions on the object, only if the user is the author.

        :param request: The request object.
        :param view: The view object.
        :param obj: The 'Post' object in question.
        :return: True if the request user is authenticated and is the
            post author, False otherwise.
        """

        # Read requests are allowed (from authenticated users)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write requests are allowed for authenticated post authors only
        return request.user == obj.author
