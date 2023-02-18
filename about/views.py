from django.shortcuts import render
from.models import About


# Create your views here.
def home(request):
    about=About
    return render(request,'home.html',{})

