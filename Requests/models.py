from django.db import models
from Program.models import Program, Student
from django_serializable_model import SerializableModel


# Create your models here.
class RequestData(SerializableModel):
    std = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    year_of_graduation = models.CharField(max_length=5)
    name_in_ar = models.CharField(max_length=100)
    name_in_en = models.CharField(max_length=100)
    cert_type = models.CharField(max_length=25)
    degree = models.CharField(max_length=25)
    copies_of_ar = models.IntegerField()
    copies_of_en = models.IntegerField()
    isAccepted = models.BooleanField(default=None, null=True)
# RequestData.objects.create(
#     std=Student.objects.get(pk=10),
#     program=Program.objects.get(pk=1)
#     ,phone='1000',
#     email='C@C.C',
#     year_of_graduation='2020',
#     name_in_ar='AR',
#     name_in_en='EN',
#     cert_type='cert_type',
#     degree='degree',
#     copies_of_ar=1,
#     copies_of_en=2,
#     )
