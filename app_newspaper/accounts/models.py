from django.db import models
from django.contrib.auth.models import AbstractUser #Importando AbstractUser para ampliar el modelo User

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True) #Agregando la edad null para el User