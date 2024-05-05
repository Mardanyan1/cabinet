from django.db import models


class CustomUser(models.Model):
    ROLES = (
        ('admin', 'Администратор'),
        ('user', 'Пользователь'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='user')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=255, blank=False, null=False, default="")
    experience = models.TextField(blank=True, null=True)
    password = models.CharField()

    def __str__(self):
        return f"{self.first_name} {self.contact_info}"
