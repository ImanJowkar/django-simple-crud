from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                cd['username'], cd['email'], cd['password'])
            messages.success(
                request, f"User {cd['username']} created successfully", extra_tags='success')
            return redirect('home')

    else:
        form = forms.UserRegistrationForm()
    return render(request, 'accounts/register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"User {cd['username']} logged in successfully", extra_tags='success')
                return redirect('home')
            else:
                messages.error(
                    request, "username or password incorrect", extra_tags='danger')
    else:
        form = forms.UserLoginForm()
    return render(request, 'accounts/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    messages.success(
        request, f"User logged out successfully", extra_tags='success')
    return redirect('home')