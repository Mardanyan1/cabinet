from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)
    contact_info = forms.CharField(max_length=100, required=True)
    experience = forms.CharField(max_length=200, required=True)

    password1 = forms.CharField(label=("password1"), strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label=("password2"), widget=forms.PasswordInput, strip=False)

    class Meta:
        model = User
        fields = ['username', 'contact_info', 'role', 'experience', 'password1', 'password2', 'is_superuser']


class CustomLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'contact_info', 'experience']
