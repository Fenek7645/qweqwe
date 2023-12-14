from django.shortcuts import render, HttpResponseRedirect

from regestration.models import User

from regestration.forms import UserLoginForm, UserRegistrationForm

from django.contrib import auth
# Создаём функции для вывода html страницы
from django. urls import reverse

def regestration(requset):
    if requset.method == "POST":
        form = UserRegistrationForm(data=requset.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('enterens'))
    else:
        form = UserRegistrationForm()
    
    context = {'form': form} 
    return render(requset, 'regestration/regestration.html', context)


def enterens(requset):
    if requset.method == 'POST':
        form = UserLoginForm(data=requset.POST)
        if form.is_valid():
            username = requset.POST['username']
            password = requset.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(requset, user)
                return HttpResponseRedirect(reverse('profile'),)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(requset, 'regestration/enterens.html', context)


def profile_view(requset):
    return render(requset, 'regestration/profile.html')