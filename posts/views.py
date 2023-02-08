from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer, UserSerializer


class PostViewSet(ModelViewSet):
    """
    Handles views for objects of the 'Post' class.

    Provides basic CRUD operations on 'Post' class objects
    using the 'PostSerializer' serializer.

    Additionally, it only allows the authors of a 'Post' object to edit it.
    Other users can only view the object.
    """
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    """
    Handles views for objects of the 'CustomUser' class.

    Provides basic CRUD operations on 'User' class objects
    using the 'UserSerializer' serializer.

    Only users with the 'Admin' permission can access this viewset.
    """
    permission_classes = (IsAdminUser, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
