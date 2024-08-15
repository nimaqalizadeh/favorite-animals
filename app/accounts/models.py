from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User's fields can be customed   
    """
    pass

    def __str__(self) -> str:
        return self.username