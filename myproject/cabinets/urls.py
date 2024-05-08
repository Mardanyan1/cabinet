from django.urls import path
from .views import register, login_view, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', login_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]
