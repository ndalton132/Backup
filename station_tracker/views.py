from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  return render(request, 'index.html')
    

  

