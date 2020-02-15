from django.shortcuts import HttpResponse
from .models import *
from json import loads
from Program.models import *


# Create your views here.
def create(request):
    map = loads(request.body.decode('UTF-8'))
    std = Student.objects.get(pk=map['std'])
    prog = ScientificStatues.objects.get(std_ref=std).dep_ref
    rd = RequestData.objects.create(
        std=std,
        program=prog,
        phone=std.phone,
        email=std.email,
        year_of_graduation=map['year_of_graduation'],
        name_in_ar=map['name_in_ar'],
        name_in_en=map['name_in_en'],
        cert_type=map['cert_type'],
        degree=prog.degree,
        copies_of_ar=map['copies_of_ar'],
        copies_of_en=map['copies_of_en'],
    )
    rd.save()
    return HttpResponse('{}'.format(rd.pk))
