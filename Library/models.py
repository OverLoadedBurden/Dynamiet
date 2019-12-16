from django.db import models
from Students.models import Student
from json import loads


# Create your models here.
class Library(models.Model):
    ref = models.ForeignKey(Student, on_delete=models.CASCADE)
    in_debt = models.TextField(default='[]')

    def __str__(self):
        end = ''
        count = len(loads(self.in_debt))
        if count == 0:
            end = 'is clear'
        else:
            suf = ''
            if count > 1:
                suf = 's'
            end = 'has {} book{}'.format(count, suf)
        return str(self.ref) + ':' + end
