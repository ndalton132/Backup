from django.urls import path
from .views import index
from . import views

urlpatterns = [
   # path('', home,name="home"),
   path('', views.index, name='home'),
   path('index/', index, name='index'),
   path('login/', views.user_login, name='login'),
   path('signup/', views.user_signup, name='signup'),
   path('logout/', views.user_logout, name='logout'),
]

