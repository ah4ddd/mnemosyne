"""
Finds the template file
Renders it into HTML
Wraps it in an HTTP response
Sends it back to the browser
"""

from django.shortcuts import render
from .models import Topic

def index(request):
    #Inside the templates/ folder, look inside the mnemosyne namespace
    return render(request, 'mnemosyne/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'mnemosyne/topics.html', context)
