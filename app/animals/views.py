from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404

from .models import Animal


class AnimalListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = "animals/list_animals.html"
    context_object_name = "animals"
    login_url = reverse_lazy("accounts:login")

    def get_queryset(self):
        return Animal.objects.filter(user=self.request.user)


class AnimalAddView(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")

    def post(self, request, *args, **kwargs):
        animal_name = request.POST.get("name")

        if Animal.objects.filter(user=request.user, name=animal_name).exists():
            return JsonResponse(
                {"error": "Animal with this name already exists."}, status=400
            )

        animal = Animal.objects.create(
            user=request.user, name=animal_name
        )

        return JsonResponse(
            {
                "name": animal.name,
                'id': animal.id
            }
        )