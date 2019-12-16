from django.db import models
# from django.core import model
import random
from json.decoder import JSONDecoder
from json import dumps
import lists
from lists import *


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    collage_NO = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


def make_random_std():
    name = make_random_name()
    passed = False
    while not passed:
        name = make_random_name()
        try:
            Student.objects.get(['name', name])
        except Exception as e:
            passed = True
    ph = ''
    passed = False
    while not passed:
        ph = make_random_ph()
        try:
            Student.objects.get(['phone', ph])
        except Exception as e:
            passed = True
    cno = 0
    passed = False
    while not passed:
        cno = random.Random().randint(100000, 999999)
        try:
            Student.objects.get(['collage_NO', cno])
        except Exception as e:
            passed = True
    email = make_email(name)
    std = Student.objects.create(name=name, email=email, collage_NO=cno, phone=ph)
    std.save()
    init_lib(std)
    init_dep(std)
    init_finance(std)


def make_email(name: str) -> str:
    l = name.split()
    ind = 0
    first = l[ind]
    ind = 1
    if first == 'عبد':
        first = first + ' ' + l[ind]
        ind = 2
    second = l[ind]

    if second == 'عبد':
        second = second + ' ' + l[ind + 1]
    i1 = -1
    try:
        i1 = en_males[males.index(first)]
    except:
        i1 = en_females[females.index(first)]
    i2 = en_males[males.index(second)]
    email = i1 + '_' + i2
    if random.Random().randint(0, 1) == 0:
        email = email + str(random.Random().randint(1992, 1998))
    end = ['yahoo', 'gmail', 'outlook', 'live']
    return email + '@' + end[random.Random().randint(0, 3)] + '.com'


def make_random_ph():
    poss = ['012', '099', '092', '091', '090', '096']
    ph = poss[random.Random().randint(0, 5)]
    ph = ph + str(random.Random().randint(1000000, 9999999))
    return ph


def make_random_name():
    gender = random.Random().randint(0, 10)
    first_name = ''
    isolate = males[:]
    if gender < 5:
        gender = 'male'
        rand = random.Random().randint(0, len(males) - 1)
        first_name = males[rand]
        isolate.pop(rand)
    else:
        gender = 'female'
        first_name = females[random.Random().randint(0, len(females) - 1)]
    name = first_name + ' '
    for x in range(0, 3):
        rand = random.Random().randint(0, len(isolate) - 1)
        name += isolate[rand] + ' '
        isolate.pop(rand)
    return name.strip()


############# init the random ScientificStatues ################
def init_dep(obj: Student):
    from Program.models import ScientificStatues, Program
    progs = Program.objects.all()
    app_loc = random.Random().randint(0, len(progs) - 1)
    app = progs[app_loc]
    courses = make_semester(app.courses)
    ScientificStatues.objects.create(std_ref=obj, dep_ref=app, GPA_details=dumps(courses))


def make_semester(courses) -> list:
    courses = JSONDecoder().decode(courses)
    ret = []
    for semester in courses:
        sem = {}
        for course in semester:
            sem[course] = random.Random().randint(35, 100)

        ret.append(sem)

    return ret


################init random Library profile################33

def init_lib(obj: Student):
    if random.Random().randint(0, 5) < 3:
        return
    from Library.models import Library
    json = []
    for i in range(0, 3):
        if random.Random().randint(0, 5) < 3:
            continue
        while True:
            book = random.Random().randint(0, len(lists.books) - 1)
            if not json.__contains__(book):
                json.append(lists.books[book])
                break
    Library.objects.create(ref=obj, in_debt=dumps(json, ensure_ascii=False), ).save()


####################init random FinanceStatuse######################

def init_finance(obj: Student):
    from Finance.models import FinanceStatues
    from Program.models import Program, ScientificStatues
    prog = ScientificStatues.objects.get(['std_ref', obj]).dep_ref
    courses = prog.courses
    semester_count = len(JSONDecoder().decode(courses))
    finance_dues = {}
    for i in range(1, semester_count + 1):
        paid = 0
        luck = random.Random().randint(1, 10)
        if luck <= 8:
            paid = prog.cost
        else:
            paid = prog.cost * (luck / 10)
        finance_dues[i] = paid
    FinanceStatues.objects.create(finance_dues=dumps(finance_dues), ref=obj)
