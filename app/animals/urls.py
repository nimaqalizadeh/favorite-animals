from django.urls import path, include

from .views import AnimalAddView, AnimalListView

app_name = "animals"

urlpatterns = [
    path("", AnimalListView.as_view(), name="list_animals"),
    path("add/", AnimalAddView.as_view(), name="add_animal"),
    # path('delete/', AnimalDeleteView.as_view(), name='delete_animal'),
    # API URLs
    path('api/', include('animals.api.v1.urls'), name='animals_api_v1')
]
