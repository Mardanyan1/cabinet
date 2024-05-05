from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser


def register(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'cabinets/register.html', {'form': form})

        # return render(request, 'cabinets/register.html')
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем на страницу входа после успешной регистраци
        return render(request, 'cabinets/register.html', {'form': form})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'cabinets/login.html')
    elif request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('contact_info')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправляем на домашнюю страницу после успешного входа
    else:
        form = CustomAuthenticationForm()
    return render(request, 'cabinets/login.html', {'form': form})
