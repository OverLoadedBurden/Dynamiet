from django.shortcuts import HttpResponse
from .models import *
from django.core.serializers import serialize


# Create your views here.
def all(request):
    return HttpResponse(serialize('json',Program.objects.all()))


def of_std(request):
    std=Student.objects.get(collage_NO=request.GET.get('id'))
    sci=ScientificStatues.objects.get(std_ref=std)
    return HttpResponse(serialize('json',[sci.dep_ref]))


def by_id(request):
    std=None
    try:
        std=Student.objects.get(collage_NO=request.GET.get('id'))
    except Exception:
        return HttpResponse('1')
    sci=None
    try:
        sci=ScientificStatues.objects.get(std_ref=std)
    except Exception:
        return HttpResponse('2')
    return HttpResponse(serialize('json',[sci]))


def create(request):
    map = loads(request.body.decode('UTF-8'))
    std = Student.objects.get(collage_NO=map['std'])
    create_bool=True
    try:
        ScientificStatues.objects.get(std_ref=std)
        create_bool=False
    except:
        pass
    if create_bool:
        ScientificStatues.objects.create(
            std_ref=std,
            dep_ref=Program.objects.get(pk=map['prog']),
            GPA_details=map['gpa']
        ).save()
        return HttpResponse('0')
    else:
        sci = ScientificStatues.objects.get(std_ref=std)
        sci.GPA_details=map['gpa']
        sci.dep_ref=Program.objects.get(pk=map['prog'])
        sci.save()
        return HttpResponse('1')
