from django.shortcuts import HttpResponse
from .models import *
from django.core.serializers import serialize
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


def check(request):
    id = request.GET.get('id')
    ret = 3
    try:
        r = RequestData.objects.get(id=id)
        if r.isAccepted is None: ret = 2
        if not r.isAccepted and r.isAccepted is not None: ret = 1
        if r.isAccepted: ret = 0
    except:
        pass
    return HttpResponse(ret)


def get(request):
    type = request.GET.get('type')
    ret = None
    if type == 'all':
        ret = (RequestData.objects.all())
    if type == 'wait':
        ret = (RequestData.objects.filter(isAccepted=None))
    if type == 'True':
        ret = (RequestData.objects.filter(isAccepted=True))
    if type == 'False':
        ret = (RequestData.objects.filter(isAccepted=False))
    return HttpResponse(serialize('json', ret))


def handle(request):
    id = request.GET.get('id')
    approve = request.GET.get('approve')
    r = RequestData.objects.get(id=id)
    if approve == '0':
        r.isAccepted = True
    else:
        r.isAccepted = False
    r.save()
    return HttpResponse('0')
