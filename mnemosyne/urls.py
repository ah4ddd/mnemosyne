"""Defines url patterns for mnemosyne"""

from django.urls import path
from . import views

app_name = 'mnemosyne'
urlpatterns = [
    #Home page
    path('', views.index, name='index')
]
