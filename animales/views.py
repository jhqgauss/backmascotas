from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from animales.models import animal
from animales.serializers import AnimalSerializer

# Create your views here.

@csrf_exempt
def animalApi(request,id=0):
    if request.method=='GET':
        animals=animal.objects.all()
        animals_serializer= AnimalSerializer(animals,many=True)
        return JsonResponse(animals_serializer.data,safe=False)
    elif  request.method=='DELETE':
        animals=animal.objects.get(AnimalId=id)
        animals.delete()
        return JsonResponse("Eliminado",safe=False)
