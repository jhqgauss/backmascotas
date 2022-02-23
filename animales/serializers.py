from rest_framework import serializers
from animales.models import animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model= animal
        fields =('AnimalId','name','raza')
