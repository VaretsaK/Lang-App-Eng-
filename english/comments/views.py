from django.shortcuts import render
from django.http import HttpResponse


def comment(request):
    return HttpResponse("Comments here!")
