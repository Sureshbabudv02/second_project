from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def musician(request):
    return HttpResponse('<h1>Hello! This is Musician</h1>')

def suresh(request):
    return HttpResponse('<h1>Hi! This is Suresh</h1>')
