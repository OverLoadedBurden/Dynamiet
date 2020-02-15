from django.shortcuts import HttpResponse
from json import loads, dumps
from .models import *
from django.core.serializers import serialize


# Create your views here.
def cost(request):
    id = request.GET.get('id')
    std = Student.objects.get(collage_NO=id)
    prog = ScientificStatues.objects.get(['std_ref', std]).dep_ref
    return HttpResponse(f'{prog.cost}')


def by_id(request):
    std = None
    id = request.GET.get('id')
    try:
        std = Student.objects.get(collage_NO=id)
    except Exception:
        return HttpResponse('1')
    sci = None
    try:
        sci = FinanceStatues.objects.get(ref=std)
    except Exception:
        return HttpResponse('2')
    return HttpResponse(serialize('json', [sci]))


def create(request):
    map = loads(request.body.decode('UTF-8'))
    std = Student.objects.get(collage_NO=map['std'])
    create_bool = True
    try:
        FinanceStatues.objects.get(ref=std)
        create_bool = False
    except:
        pass
    if create_bool:
        FinanceStatues.objects.create(
            ref=std,
            finance_dues=map['dues']
        ).save()
        return HttpResponse('0')
    else:
        fs = FinanceStatues.objects.get(ref=std)
        fs.finance_dues = map['dues']
        fs.save()
        return HttpResponse('1')
