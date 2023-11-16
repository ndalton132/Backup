from django.urls import path, include
from location_search import views as searchViews
from . import views

urlpatterns = [
   # path('', home,name="home"),
   path('', views.index, name='home'),
   path('login/', views.user_login, name='login'),
   path('signup/', views.user_signup, name='signup'),
   path('logout/', views.user_logout, name='logout'),

    #Find Gas stations button
   path('location_search/', searchViews.map_view, name = "findGas"),
  path('location_search/', include('location_search.urls')),
    

   path('feedback/', views.feedback_form, name="feedback"),
   path('station-tracker/', views.map_view, name="station-tracker"),
]

