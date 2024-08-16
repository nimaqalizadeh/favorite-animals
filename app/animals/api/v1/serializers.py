from rest_framework import serializers
from ...models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'user', 'name']
        read_only_fields = ['id', 'user'] 

    