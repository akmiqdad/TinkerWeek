from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Event, Participent
from .forms import RegForm
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
    if request.POST:
        form = RegForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('registration')
        else:
            form=RegForm()
            context['form'] = form
    else:
        form=RegForm(
            initial={
                'name':'',
                'institute_name':'',
                'year':'',
                'email':'',
                'phone':''
                'event'
            }
        )
        context['form']=form

    return render(request,'registration.html', context)

