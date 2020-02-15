from django.conf.urls import url
from .views import *
# from .models import has_issues


def check(request):
    std = Student.objects.get(pk=request.GET.get('id'))
    print(has_issues(std))
    if has_issues(std):
        return HttpResponse('1')
    else:
        return HttpResponse('0')


urlpatterns = [
    # url('check', check),
    # url('get', all),
    # url('of_std', of_std),
    # url('by_id', by_id),
    url('create', create),
]
