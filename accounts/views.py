from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    #register a new user
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm()
    else:
        form = UserCreationForm()
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('mnemosyne:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
