from django import forms
from .models import GasStation

class GasPriceUpdateForm(forms.ModelForm):
    class Meta:
        model = GasStation
        fields = ['regular_gas_price', 'premium_gas_price', 'diesel_price']
