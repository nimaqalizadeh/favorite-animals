from django.urls import path, include

from .views import NoteAddView, NoteListView

app_name = "notes"

urlpatterns = [
    path("", NoteListView.as_view(), name="list_notes"),
    path("add/", NoteAddView.as_view(), name="add_note"),
    # API URLs
    path('api/', include('notes.api.v1.urls'), name='notes_api_v1')
]
