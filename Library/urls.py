from django.conf.urls import url
from .views import *


def check(request):
    std = Student.objects.get(pk=request.GET.get('id'))
    lib = Library.objects.get(ref=std)
    count = len(loads(lib.in_debt))
    if count == 0:
        return HttpResponse('0')
    else:
        return HttpResponse('1')


urlpatterns = [
    url('by_id', by_id),
    url('create', create),
    url('check', check),
]
