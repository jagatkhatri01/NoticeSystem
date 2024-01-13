from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.
class NoticeBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notices_uploaded', default=1)

    def __str__(self) -> str:
        return self.title