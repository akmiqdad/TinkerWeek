from django.shortcuts import render
from django.http import HttpResponse

from .models import Event, Participent
# Create your views here.

def home(request):
    Events  = Event.objects.all()
    context = {}
    context['Events'] = Events
    return render(request,'home.html', context)

def registration(request):
    Participents  = Participent.objects.all()
    context = {}
    context['Participents'] = Participents
    return render(request,'home.html', context)

