from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

def hello(request):
    return HttpResponse("Hello World! You are at the todo index")

@login_required()
def hello_protected(request):
    return HttpResponse("Hello World! You are at the todo index. Shhh! This page is protected")


def index(request):
    return HttpResponse("welcome")