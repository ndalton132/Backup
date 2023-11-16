from django.urls import path
#from .views import home
from . import views

urlpatterns = [
   # path('', home,name="home"),
   path('', views.index, name='home'),
   path('login/', views.user_login, name='login'),
   path('signup/', views.user_signup, name='signup'),
   path('logout/', views.user_logout, name='logout'),
   path('update_gas_prices/', views.update_gas_prices, name="update_gas_prices"),
   path('feedback/', views.feedback_form, name="feedback"),
]

