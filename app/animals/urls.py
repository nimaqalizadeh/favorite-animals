from django.contrib import admin
from django.urls import path, include
from .views import AnimalListView, AnimalAddView

app_name = 'animals'

urlpatterns = [
    path('', AnimalListView.as_view(), name='list_animals'),
    path('add/', AnimalAddView.as_view(), name='add_animal'),
    # path('delete/<int:animal_id>/', AnimalDeleteView.as_view(), name='delete_animal')
]