from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Заказчик'),
        ('performer', 'Исполнитель'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    contact_info = models.CharField(max_length=100)
    experience = models.CharField(max_length=200)

    def __str__(self):
        return self.username
