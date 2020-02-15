from django.db import models
from Students.models import Student
from json import loads
from django_serializable_model import SerializableModel


# Create your models here.
class Program(SerializableModel):
    name = models.CharField(max_length=30)
    courses = models.TextField()
    degree = models.CharField(max_length=30)
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class ScientificStatues(SerializableModel):
    std_ref = models.ForeignKey(Student, on_delete=models.CASCADE)
    dep_ref = models.ForeignKey(Program, on_delete=models.CASCADE)
    GPA_details = models.TextField()

    def __str__(self):
        end = ''
        if has_issues(self.std_ref):
            end = '-' + str(issues_count(self))
        else:
            end = str(self.get_gpa())
        return str(self.std_ref) + ' : ' + end

    def get_gpa(self) -> float:
        details = loads(self.GPA_details)
        semester_count = len(details)
        gpa = 0
        for semester_courses in details:
            semetergpa = 0
            for course in semester_courses.keys():
                semetergpa = semetergpa + int(semester_courses[course])

            semetergpa = semetergpa / len(semester_courses)
            gpa = gpa + semetergpa
        # print(gpa)
        # print(gpa / semester_count)
        # print((gpa / semester_count) / 25)
        return (gpa / semester_count) / 25


def issues_count(sc: ScientificStatues) -> int:
    gpa = loads(sc.GPA_details)
    ret = 0
    for sem in gpa:
        for course in sem:
            if int(sem[course]) < 40:
                ret = ret + 1
    return ret


def has_issues(std: Student):
    sc = ScientificStatues.objects.get(['std_ref', std])
    gpa = loads(sc.GPA_details)
    passed = True
    for sem in gpa:
        for course in sem.keys():
            passed = passed and (int(sem[course]) >= 40)
        if not passed:
            break
    return not passed
