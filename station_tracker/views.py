from django.shortcuts import render
from .models import GasStation
from .forms import GasPriceUpdateForm

# Create your views here.
def home(request):
  return render(request, 'index.html')


def update_gas_prices(request):
  if request.method == 'POST':
    form = GasPriceUpdateForm(request.POST)
    if form.is_valid():
        form.save()
  Gas_Price_Update_Form = GasPriceUpdateForm()
  return render(request, 'update_gas_prices.html', {"Gas_Price_Update_Form": Gas_Price_Update_Form})