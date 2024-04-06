from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[('member', 'Member'), ('CR', 'Class Representative'), ('dean', 'Dean')], default='member')
    department = models.CharField(max_length=50, default=1)
    semester = models.IntegerField(default=1)