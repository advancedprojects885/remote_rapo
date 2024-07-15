from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def hydjobs(request):
    s='hyderabad jobs information is very important to youth students'
    return HttpResponse(s)

def punejobsinfo(request):
    h='pune jobs information is very good fantatstic information provided by the governament of pune and they are very kind to help to us in the case of jobs portal'
    return HttpResponse(h)

def mumbaijobsinfo(request):
    p='mumbai jobs information'
    return HttpResponse(p)
