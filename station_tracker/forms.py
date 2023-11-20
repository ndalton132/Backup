from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.forms import ModelForm, Textarea
from .models import Feedback

class SignupForm(UserCreationForm):
  email = forms.EmailField(required=True)
  
  class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']
      
  def save(self, commit=True):
      user = super(SignupForm, self).save(commit=False)
      user.email = self.cleaned_data['email']
      if commit:
        user.save()
        return user
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class GasPriceUpdateForm(forms.ModelForm):
  class Meta:
      model = models.Gas_Station
      fields = ['regular_gas_price', 'premium_gas_price', 'diesel_price', 'station_name']

class FeedbackForm(ModelForm):
  class Meta:
    model = Feedback
    fields = ['name', 'email', 'phone', 'comments', 'gasStationAddr']
    widgets = {
      'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}),
      'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email'}),
      'phone' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Phone Number'}),
      'comments': Textarea(attrs= {'placeholder':'Leave a comment/review', 'class':'form-control', 'rows':'5'}),
      'gasStationAddr' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Gas Station Address'}),
    }
 
