from django.urls import path
from .views import *
 
urlpatterns = [
    path('', EmailView.as_view()),
]