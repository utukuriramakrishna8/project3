from django.shortcuts import render
from django.http import HttpResponse

def msd(request):
    return HttpResponse('<Captain Cool')
def virat(request):
    return HttpResponse('<h1><b><marquee>Virat on fire</marquee></b></h1>')
def rohit(request):
    return HttpResponse('Hitman captain')
