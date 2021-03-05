from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, My fun. You're at the Test index.")
