from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def prabhas(request):
    return HttpResponse("<marquee><h1>prabhas</h1></marquee>")