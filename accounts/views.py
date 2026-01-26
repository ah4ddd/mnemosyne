from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#register a new user
def register(request):
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #log user in and then redirect to home page
            login(request, new_user)
            return redirect('mnemosyne:index')
    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
