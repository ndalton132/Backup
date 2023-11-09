from django.urls import path
from .views import update_gas_prices, home

urlpatterns = [
    path('', home, name="home"),
    path('update_gas_prices/', update_gas_prices, name="update_gas_prices"),
]
