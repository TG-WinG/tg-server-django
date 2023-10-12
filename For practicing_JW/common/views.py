from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserCreationForm
import socket, time, os, asyncio

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None and user.is_authenticated:
                login(request, user)
            else:
                return render(request, 'common/signup.html', {'form': form})
             # 로그인
            return redirect('Start:index')
    else:
        form = UserCreationForm()
    return render(request, 'common/signup.html', {'form': form})

def to_mainpage(request):
    return redirect('main:index')

