from django.urls import path
from .views import home
from location_search import views


urlpatterns = [
   path('', home,name="home"),
    #path('buttonClick/<str:param>/', views.buttonClick, name='buttonClick'),
   path('location_search/', views.printHello, name = "connect"),
   path('location_search/add', views.SearchCreate.as_view, name = "add-search")
    
]