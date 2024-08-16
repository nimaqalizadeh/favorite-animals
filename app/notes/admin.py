from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at"]


admin.site.register(Note, NoteAdmin)
