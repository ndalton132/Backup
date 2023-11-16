from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
#from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Feedback, AboutUs
from django.http import HttpResponse


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# Main page
def main(request):
  # Retrieve user information
  user = request.user

  # Pass user information to the template
  context = {'user': user}
  return render(request, 'main.html', context)

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
               # form.save()
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
   # return render(request, 'login.html', {'form': form}, {'user': request.user})
        return render(request, 'login.html', {'user': request.user, 'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('index')


def feedback_form(request):
  return render(request, 'feedback.html')

def user_about(request):
  return render(request, 'about.html')
