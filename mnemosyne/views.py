"""
Finds the template file
Renders it into HTML
Wraps it in an HTTP response
Sends it back to the browser
"""

from django.shortcuts import redirect, render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    #add new topic
    if request.method != 'POST':
        form = TopicForm() # create a blank form if no data submitted

    else:# POST data submitted; create a blank form
        form =TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mnemosyne:topics')
    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'mnemosyne/new_topic.html', context)

def new_entry(request, topic_id):
    '''Add a new entry for a particular topic'''
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('mnemosyne:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'mnemosyne/new_entry.html', context)

def edit_entry (request, entry_id):
    '''editing an existing entry'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #initial form; prefill form with the current entry
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mnemosyne:topic', topic_id=topic.id) # type: ignore

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'mnemosyne/edit_entry.html', context)
