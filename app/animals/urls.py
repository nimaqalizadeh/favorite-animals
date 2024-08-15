from django.urls import path

from .views import AnimalAddView, AnimalListView

app_name = "animals"

urlpatterns = [
    path("", AnimalListView.as_view(), name="list_animals"),
    path("add/", AnimalAddView.as_view(), name="add_animal"),
    # path('delete/<int:animal_id>/', AnimalDeleteView.as_view(), name='delete_animal')
]
