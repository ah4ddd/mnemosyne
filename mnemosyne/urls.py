"""Defines url patterns for mnemosyne"""

from django.urls import path #Django's URL tool
from . import views #apps view

app_name = 'mnemosyne' #name spacing
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #path to all topics
    path('topics/', views.topics, name='topics'),
    #detail page for single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for new topic
    path('new_topic/', views.new_topic, name='new_topic')
]

