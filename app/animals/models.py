from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    """
    Defines animal category: Mamal, Bird, Fish, Reptile and Amphibian.
    These categoires are mapped to numbers to have enumeration
    """
    class animal_category(models.TextChoices):
        MAMAL = "Mamal"
        BIRD = "Bird"
        FISH = "Fish"
        REPTILE = "Reptile"
        AMPHIBIAN = "Amphibian"
    
    animal_type = models.CharField(unique=True, max_length=15, choices=animal_category.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.animal_type
    

class Animal(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.animal} - {self.user}"

