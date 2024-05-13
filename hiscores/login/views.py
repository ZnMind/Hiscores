from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import PlayerSignUpForm, PlayerLoginForm

def register(request):
    if request.method == 'POST':
        form = PlayerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creation of player model will go here
            login(request, user)  
            return redirect('home')  
    else:
        form = PlayerSignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def player_login(request):
    if request.method == 'POST':
        form = PlayerLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            username = form.cleaned_data['username']
            
            user = authenticate(username=username, password=password)
            
            login(request, user)
            return redirect('home')
    else:
        form = PlayerLoginForm()
    return render(request, 'registration/login.html', {'form': form})
