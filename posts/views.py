from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer


class PostList(ListCreateAPIView):
    """
    This class-based view is used to handle requests for listing all posts
    and creating new posts.

    It inherits from the ListCreateAPIView generic view provided by the
    Django REST framework, which provides the basic implementation for
    handling GET and POST requests for listing and creating new instances
    of a model.

    The permission required to access this view is that the user must be
    authenticated.

    Attributes:
        permission_classes: A tuple of permission classes that define the
            permission required to access this view.
        queryset: A queryset that contains all the posts in the database.
        serializer_class: The serializer class used to convert the Post model
            into a JSON format.
    """
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    This class-based view is used to handle requests for retrieving, updating,
    and deleting a specific post.

    It inherits from the 'RetrieveUpdateDestroyAPIView' generic view provided
    by the Django REST framework, which provides the basic implementation for
    handling GET, PUT, PATCH, and DELETE requests for a specific instance
    of a model.

    The permission required to access this view is that the user must either
    be the author of the post or the request method must be a safe method
    (GET, HEAD, or OPTIONS).

    Attributes:
        permission_classes: A tuple of permission classes that define the
            permission required to access this view.
        queryset: A queryset that contains all the posts in the database.
        serializer_class: The serializer class used to convert the Post model
            into a JSON format.
    """
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
