from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Esta é a index')