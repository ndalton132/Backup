from . import models
from django.shortcuts import render
import requests
from django.views.generic.edit import UpdateView,CreateView
from .forms import SearchForm




def printHello(request):
    return render(request,'stuff.html')

class SearchCreate(CreateView):
    model = models.Search
    fields = ["location","range"]
