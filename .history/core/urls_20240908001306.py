from django.urls import path
from .views import *
 
urlpatterns = [
    path('', IndexView.as_view()),
    path('acompanhar/<int:id', EmailView.as_view(), name='acompanhar'),
]