from django.conf.urls import url
from .views import *


urlpatterns = [
    url('check', check),
    url('get', get),
    url('handle', handle),
    # url('by_id', by_id),
    url('create', create),
]
