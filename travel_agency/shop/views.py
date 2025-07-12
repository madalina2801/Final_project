from django.shortcuts import render
from django.http import HttpResponse

def aaa(request):
    return HttpResponse("This is aaa page, returned by aaa view!")

# Create your views here.
