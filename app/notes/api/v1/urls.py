from django.urls import path
from .views import NoteListCreateView, NoteReadUpdateDelView

app_name = "api-v1"

urlpatterns = [
    path('v1/list', NoteListCreateView.as_view(), name='note_create'),
    path('v1/detail/<int:pk>/', NoteReadUpdateDelView.as_view(), name='note_detail'),
]
