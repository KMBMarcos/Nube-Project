from django.shortcuts import render

# View example
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index")
