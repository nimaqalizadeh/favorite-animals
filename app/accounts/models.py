# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager


# class User(AbstractUser):
#     """
#     User's fields can be customed   
#     """
#     username = models.CharField(max_length=255, unique=True)
#     USERNAME_FIELD = 'username'
     
#     objects = CustomUserManager() 

#     def __str__(self) -> str:
#         return self.username