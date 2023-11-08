
from django.urls import path
from .views import *

urlpatterns = [
    path('', identify_disease, name='identify-disease'),
]
