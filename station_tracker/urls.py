from django.urls import path
from .views import home
from location_search import views as searchViews


urlpatterns = [
   path('', home,name="home"),
   path('location_search/', searchViews.searchPage, name = "findGas"),

    
]