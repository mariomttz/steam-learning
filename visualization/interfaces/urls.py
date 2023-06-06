# Libraries and packages
from interfaces.views import index
from django.urls import path

urlpatterns = [
    path('', index, name = 'home'),
]