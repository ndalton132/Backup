from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class FeedbackForm(ModelForm):
  class Meta:
    model = Feedback
    fields = ['name', 'email', 'phone', 'comments', 'gasStationAddr']
    widgets = {
      'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name', 'id':'name'}),
      'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email', 'id':'email'}),
      'phone' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Phone Number', 'id':'phone'}),
      'comments': Textarea(attrs= {'placeholder':'Leave a comment/review', 'class':'form-control', 'rows':'5', 'id':'comments'}),
      'gasStationAddr' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Gas Station Address', 'id':'gasStationAddr'}),
    }
 