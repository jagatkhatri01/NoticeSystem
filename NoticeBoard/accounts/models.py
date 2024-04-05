from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # forget_password_token = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=[('member', 'Member'), ('CR', 'Class Representative'), ('dean', 'Dean')], default='member')
    department = models.CharField(max_length=50)
    semester = models.IntegerField()