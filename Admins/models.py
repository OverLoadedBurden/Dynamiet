from django.db import models
from django_serializable_model import SerializableModel


# Create your models here.
class User(SerializableModel):
    name = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
