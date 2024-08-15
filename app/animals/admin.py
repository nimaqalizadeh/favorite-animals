from django.contrib import admin
from .models import Category, Animal, Favorite


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['animal_type', 'created_at', 'updated_at']


class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'user', 'created_at', 'updated_at' ]


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'animal', 'created_at', 'updated_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Favorite, FavoriteAdmin)