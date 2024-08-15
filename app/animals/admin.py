from django.contrib import admin

from .models import Animal

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['animal_type', 'created_at', 'updated_at']


class AnimalAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at"]


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Animal, AnimalAdmin)
