from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework import permissions, serializers
from ...models import Note
from .serializers import NoteSerializer


class NoteListCreateView(ListCreateAPIView):
    """
    Create notes
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        note = serializer.validated_data.get('name')
        if Note.objects.filter(user=self.request.user, name=note).exists():
            raise serializers.ValidationError({'detail': f'The {note} already exists.'})     
        serializer.save(user=self.request.user)


class NoteReadUpdateDelView(RetrieveUpdateDestroyAPIView):
    """
    Read, Update and Delete notes
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
