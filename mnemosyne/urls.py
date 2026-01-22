"""Defines url patterns for mnemosyne"""

from django.urls import path #Django's URL tool
from . import views #apps view

app_name = 'mnemosyne' #name spacing
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #path to all topics
    path('topics/', views.topics, name='topics'),
]
