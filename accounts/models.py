from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A class-based model that serves as a customized implementation of
    a user in the project, providing additional functionality and flexibility.

    It inherits Django's 'AbstractUser' class, which provides the base fields
    for a user, such as 'username' and 'password', by adding a 'name' field,
    allowing the user's name storage in the database.

    Attributes:
        name: The user name.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )
