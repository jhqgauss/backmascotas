from django.db import models

# Create your models here.

class animal(models.Model):
    AnimalId= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    raza= models.CharField(max_length=100)