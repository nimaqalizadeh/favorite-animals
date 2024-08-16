from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404

from .models import Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/list_notes.html"
    context_object_name = "notes"
    login_url = reverse_lazy("accounts:login")

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteAddView(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")

    def post(self, request, *args, **kwargs):
        note_name = request.POST.get("name")

        if Note.objects.filter(user=request.user, name=note_name).exists():
            return JsonResponse(
                {"error": f"Note: {note_name} already exists."}, status=400
            )

        note = Note.objects.create(
            user=request.user, name=note_name
        )

        return JsonResponse(
            {
                "name": note.name,
                'id': note.id
            }
        )