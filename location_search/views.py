from . import models
from django.shortcuts import render
import requests
from django.views.generic.edit import UpdateView,CreateView
from .forms import SearchForm




def searchPage(request):
    return render(request,'stuff.html')

def SearchEntry(request):
    form = UploadForm(request.Post, request.Files)
    print(request.FILES)
    return
