from django.urls import path
from .views import *
 
urlpatterns = [
    path('', IndexView.as_view()),
    path('acompanhar/', EmailView.as_view()),
]