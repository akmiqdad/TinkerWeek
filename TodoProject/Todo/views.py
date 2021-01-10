from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
from .forms import ToDoForm

# Create your views here.

def home(request):
    context = {}
    todos  = Todo.objects.all()
    context['todos'] = todos
    if request.POST:
        form = ToDoForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ToDoForm()
            context['form'] = form
    else:
        form = ToDoForm(
            initial={
                'titile': '',
                'description': ''
            }
        )
        context['form'] = form
    return render(request,'home.html', context)