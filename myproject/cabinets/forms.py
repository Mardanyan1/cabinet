from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'contact_info', 'experience', 'password']


class CustomAuthenticationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['contact_info', 'password']