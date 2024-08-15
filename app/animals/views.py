from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animal


class AnimalListView(LoginRequiredMixin, ListView ):
    model = Animal
    template_name = 'animals/list_animals.html'
    context_object_name = 'animals'
    login_url = reverse_lazy('accounts:login')

    def get_queryset(self):
        return Animal.objects.filter(user=self.request.user)


# class AnimalAddView(LoginRequiredMixin, CreateView):
#     model = Animal
#     fields = ['animal']  # No fields required from the user, as it's a simple association
#     success_url = reverse_lazy('list_animals')

#     def form_valid(self, form):
#         animal = Animal.objects.get(id=self.kwargs['animal_id'])
#         form.instance.user = self.request.user
#         form.instance.animal = animal
#         # Ensure that this association does not already exist
#         if not Animal.objects.filter(user=self.request.user, animal=animal).exists():
#             return super().form_valid(form)
#         else:
#             return HttpResponseRedirect(self.success_url)


# class AnimalDeleteView(DeleteView, LoginRequiredMixin):
#     model = Favorite
#     success_url = reverse_lazy('list_animal')

#     def get_object(self, queryset=None):
#         animal = Animal.objects.get(id=self.kwargs['animal_id'])
#         return Favorite.objects.filter(user=self.request.user, animal=animal).first()


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import Animal


@method_decorator(require_POST, name='dispatch')
class AnimalAddView(LoginRequiredMixin, View):
    login_url = reverse_lazy('accounts:login')

    def post(self, request, *args, **kwargs):
        animal_name = request.POST.get('name')
        category_id = request.POST.get('category_id')

        # Check if the animal already exists for this user
        if Animal.objects.filter(user=request.user, name=animal_name).exists():
            return JsonResponse({'error': 'Animal with this name already exists.'}, status=400)

        # Create the new animal
        animal = Animal.objects.create(user=request.user, name=animal_name, category=category)

        # Return the newly created animal data
        return JsonResponse({
            'id': animal.id,
            'name': animal.name,
        })

