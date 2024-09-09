from django.urls import path
from .views import *
 
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('acompanhar/<int:pk>/', EmailView.as_view(), name='acompanhar'),
]