# from django.contrib.auth.models import BaseUserManager


# class CustomUserManager(BaseUserManager):
#     """
#     A user model manager for authentication with username
#     """
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError("The Email field must be set")
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, password, **extra_fields)