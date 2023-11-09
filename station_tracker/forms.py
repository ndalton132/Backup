
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class GasPriceUpdateForm(forms.ModelForm):
  class Meta:
      model = models.GasStation
      fields = ['regular_gas_price', 'premium_gas_price', 'diesel_price']