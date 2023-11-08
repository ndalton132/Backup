from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Feedback


# Create your views here.
def home(request):
  return render(request, 'index.html')

def feedback_form(request):
  return render(request, 'feedback.html')