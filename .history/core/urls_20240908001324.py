from django.urls import path
from .views import *
 
urlpatterns = [
    path('', IndexView.as_view()),
    path('acompanhar/<int:pk', EmailView.as_view(), name='acompanhar'),
]