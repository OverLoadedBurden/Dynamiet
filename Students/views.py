from django.shortcuts import HttpResponse
from .models import Student
from django.core.serializers import serialize
from json import loads


# Create your views here.
def get(request) -> HttpResponse:
    return HttpResponse(serialize('json', [Student.objects.get(pk=request.GET.get('id'))]))


def by_name(request) -> HttpResponse:
    return HttpResponse(serialize('json', Student.objects.filter(name__contains=request.GET.get('name'))))


def by_id(request) -> HttpResponse:
    return HttpResponse(serialize('json', Student.objects.filter(collage_NO__contains=request.GET.get('id'))))


def check(request) -> HttpResponse:
    try:
        Student.objects.get(collage_NO=request.GET.get('id'))
        return HttpResponse('0')
    except Exception:
        return HttpResponse('1')


def create(request):
    map = loads(request.body.decode('UTF-8'))
    Student.objects.create(
        name=map['name'],
        collage_NO=int(map['collage_NO']),
        email=map['email'],
        phone=int(map['phone'])
    ).save()
    return HttpResponse('0')


def delete(request) -> HttpResponse:
    try:
        Student.objects.get(collage_NO=request.GET.get('id')).delete()
        return HttpResponse('0')
    except Exception:
        return HttpResponse('1')
