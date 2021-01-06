from django.shortcuts import render
from django.http import HttpResponse

from .models import Event
# Create your views here.

def home(request):
    Events  = Event.objects.all()
    context = {}
    context['Events'] = Events
    return render(request,'home.html', context)

