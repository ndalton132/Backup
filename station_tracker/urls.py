from django.urls import path
from .views import index, main
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('index/', index, name='index'),
   path('main/', main, name='main'),
   path('login/', views.user_login, name='login'),
   path('signup/', views.user_signup, name='signup'),
   path('logout/', views.user_logout, name='logout'),
   path('feedback/', views.feedback_form, name="feedback"),
   path('about/', views.user_about, name="about"),
]

