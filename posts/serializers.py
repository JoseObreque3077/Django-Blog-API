from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostSerializer(ModelSerializer):
    """
    This serializer class is used to convert the Post model into a JSON format
    that can be used in the API views. It defines the fields to be included
    in the serialized data and the corresponding model.
    """
    class Meta:
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at'
        )
        model = Post


class UserSerializer(ModelSerializer):
    """
    This serializer class is used to convert the 'CustomUser' model into a
    JSON format that can be used in the API views. It defines the fields to be
    included in the serialized data and the corresponding model.
    """
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username'
        )
