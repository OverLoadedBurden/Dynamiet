from django.conf.urls import url
from .views import *


urlpatterns = [
    url('check', check),
    url('get', get),
    url('handle', handle),
    url('pay', pay),
    url('create', create),
]
