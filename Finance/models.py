from django.db import models
from Students.models import Student
from json import loads
from Program.models import Program, ScientificStatues


# Create your models here.
class FinanceStatues(models.Model):
    ref = models.ForeignKey(Student, on_delete=models.CASCADE)
    finance_dues = models.TextField()

    def __str__(self):
        end = ''
        if has_issues(self.ref):
            end = 'has issues.'
        else:
            end = 'is fine.'
        return str(self.ref) + ' : ' + end


def has_issues(std: Student) -> bool:
    obj = FinanceStatues.objects.get(['ref', std])
    dues = loads(obj.finance_dues)
    prog = ScientificStatues.objects.get(['std_ref', std]).dep_ref
    cost = prog.cost
    sc = len(loads(prog.courses))
    ret = True
    for i in range(1, sc + 1):
        ret = ret and (dues[str(i)] == cost)
    print(dues)
    return not ret
