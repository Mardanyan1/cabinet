from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm


def register(request):
    # if request.method == 'POST':
    #     form = CustomRegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         # Пример редиректа на страницу профиля после успешной регистрации
    #         return redirect('profile')
    # else:
    #     form = CustomRegistrationForm()
    # return render(request, 'cabinets/register.html', {'form': form})
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                return redirect('profile')  # Предполагая, что 'profile' - это правильный URL
            except Exception as e:
                print("Ошибка при сохранении пользователя:", e)  # Запись ошибки в лог
                # Можно также вернуть ответ с сообщением об ошибке
        else:
            print("Форма не прошла валидацию:", form.errors)  # Запись ошибок формы для отладки
            error_message = "Форма не прошла валидацию: {}".format(form.errors)

            return HttpResponse(error_message)
    else:
        form = CustomRegistrationForm()
    return render(request, 'cabinets/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Пример редиректа на страницу профиля после успешного входа
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'cabinets/login.html', {'form': form})


def profile(request):
    return render(request, 'cabinets/profile.html')

