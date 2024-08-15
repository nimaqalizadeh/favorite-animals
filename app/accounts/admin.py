from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
   model = User
   list_display = ['username', 'first_name', 'last_name']
   list_filter = ['username']


admin.site.register(User, CustomUserAdmin)
