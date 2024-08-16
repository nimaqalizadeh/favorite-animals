from django.urls import path
from .views import AnimalListCreateView, AnimalReadUpdateDelView

app_name = "api-v1"

urlpatterns = [
    path('v1/list', AnimalListCreateView.as_view(), name='animal_create'),
    path('v1/detail/<int:pk>/', AnimalReadUpdateDelView.as_view(), name='animal_detail'),
]
