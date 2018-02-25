# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'hello.html')


def add(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))


def home(request):
    tutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': tutorialList})
