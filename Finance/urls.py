from django.conf.urls import url
from .views import *
from .models import *


def check(request):
    std = Student.objects.get(pk=request.GET.get('id'))
    if has_issues(std):
        return HttpResponse('1')
    else:
        return HttpResponse('0')


urlpatterns = [
    url('check', check),
    url('by_id', by_id),
    url('create', create),
    url('cost', cost)
]
