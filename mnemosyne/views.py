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

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') # type: ignore
    context = {'topic': topic, 'entries': entries}
    return render(request, 'mnemosyne/topic.html', context)
