# Generated by Django 4.2.11 on 2024-05-06 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets', '0005_customuser_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
