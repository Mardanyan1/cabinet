from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('login')
            except Exception as e:
                print("Ошибка при сохранении пользователя:", e)
        else:
            print("Форма не прошла валидацию:", form.errors)
            error_message = "Форма не прошла валидацию: {}".format(form.errors)

            return HttpResponse(error_message)
    else:
        form = CustomRegistrationForm()
    return render(request, 'cabinets/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user_data = get_user_model().objects.get(username=username)
            return render(request, 'cabinets/profile.html', {'username': user_data})
        else:
            return HttpResponse("there is no that user")
    else:
        form = AuthenticationForm()
    return render(request, 'cabinets/login.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user
    print("edit profile COME")
    if request.method == 'POST':
        print("post method COME")
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            print("form valid COME")
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=user)

    return redirect('profile')