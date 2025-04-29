from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login


# Create your views here.

def hello(request):
    return HttpResponse("Hello World! You are at the todo index")

@login_required()
def hello_protected(request):
    return HttpResponse("Hello World! You are at the todo index. Shhh! This page is protected")


def index(request):
    return HttpResponse("welcome")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hello_protected')
         
        else:
            form = UserRegistrationForm()
    return render(request, 'todoapp/register.html', {'form': form})