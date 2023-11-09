from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    location = forms.TextInput()
    range = forms.TextInput

    class Meta:
        model = Search
        fields = ['location', 'range']
