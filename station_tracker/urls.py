from django.urls import path
from .views import home
from location_search import views as searchViews
#from .views import home
from . import views

urlpatterns = [
   # path('', home,name="home"),
   path('', views.index, name='home'),
   path('login/', views.user_login, name='login'),
   path('signup/', views.user_signup, name='signup'),
   path('logout/', views.user_logout, name='logout'),

    #Find Gas stations button
   path('location_search/', searchViews.searchPage, name = "findGas"),

    
]

