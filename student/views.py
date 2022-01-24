from django.shortcuts import render
from django.http import HttpResponse


def student_show(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>Django Tutorials by Wax30d</h1>The Digits are {0}".format(x))
