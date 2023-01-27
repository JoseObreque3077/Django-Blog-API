from django.conf import settings
from django.db import models


class Post(models.Model):
    """
    A class-based model that represents a blog post.

    Attributes:
        title: The post title.
        body: The post content.
        created_at: The creation timestamp of the blog post (auto-added).
        updated_at: The update timestamp for the blog post (auto-added).
    """
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        A method that returns the string representation of a 'Post' object.
        :return: The title of the 'Post' object.
        """
        return self.title
