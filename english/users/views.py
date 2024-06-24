from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserProfile


def index(request):
    return HttpResponse("Hi, man!")


def test(request):
    return HttpResponse("<h1> TEST </h1>")

