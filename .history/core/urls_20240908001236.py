from django.urls import path
from .views import *
 
urlpatterns = [
    path('acompanhar/', Index.as_view()),
    path('acompanhar/', EmailView.as_view()),
]