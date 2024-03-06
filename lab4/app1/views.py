from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
   return HttpResponse( '<h1>This is a site to calculate tax</h1>')
    
taxR = 0.15
def cal(request , x):
    afterTAX = x + (x*taxR)
    return HttpResponse(f"the price eith 15% is {afterTAX} ")

def tax(request):
     return HttpResponse(request, f'the tax rate {taxR}')





