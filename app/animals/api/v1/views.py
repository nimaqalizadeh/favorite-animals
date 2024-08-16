from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework import permissions, serializers
from ...models import Animal
from .serializers import AnimalSerializer


class AnimalListCreateView(ListCreateAPIView):
    """
    Create animals
    """
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Animal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        animal = serializer.validated_data.get('name')
        if Animal.objects.filter(user=self.request.user, name=animal).exists():
            raise serializers.ValidationError({'detail': f'The {animal} already exists.'})     
        serializer.save(user=self.request.user)


class AnimalReadUpdateDelView(RetrieveUpdateDestroyAPIView):
    """
    Read, Update and Delete animals
    """
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Animal.objects.filter(user=self.request.user)
