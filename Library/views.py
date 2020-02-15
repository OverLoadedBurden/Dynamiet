from django.shortcuts import HttpResponse
from .models import Library, Student
from json import loads
from django.core.serializers import serialize


# Create your views here.
def by_id(request):
    std=None
    id=request.GET.get('id')
    try:
        std=Student.objects.get(collage_NO=id)
    except Exception:
        return HttpResponse('1')
    sci=None
    try:
        sci=Library.objects.get(ref=std)
    except Exception:
        return HttpResponse('2')
    return HttpResponse(serialize('json',[sci]))


def create(request):
    map=loads(request.body.decode('UTF-8'))
    std=Student.objects.get(collage_NO=map['collage_NO'])
    create_bool=True
    try:
        Library.objects.get(ref=std)
        create_bool=False
    except:
        pass
    if create_bool:
        Library.objects.create(
            ref=std,
            in_debt=map['in_debt']
        ).save()
        return HttpResponse('0')
    else:
        l = Library.objects.get(ref=std)
        print(map['in_debt'])
        l.in_debt=map['in_debt']
        l.save()
        return HttpResponse('1')
