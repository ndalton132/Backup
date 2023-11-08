from django.urls import path
from .views import home, feedback_form

urlpatterns = [
  path('', home, name="home"),
  path('feedback/', feedback_form, name="feedback")
]