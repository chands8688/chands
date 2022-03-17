from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chands(request):
    return HttpResponse('<h1>This is chandu yalakurthi<h1>')
    