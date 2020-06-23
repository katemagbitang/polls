from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todoView(request):
    return HttpResponse('hello, this is the to-do page')
