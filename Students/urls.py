from django.conf.urls import url
from .views import *

urlpatterns = [
    url('get', get),
    url('by_name', by_name),
    url('by_id', by_id),
    url('check', check),
    url('delete', delete),
    url('create/', create),
]
