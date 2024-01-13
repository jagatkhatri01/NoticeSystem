from django.db import models
from accounts.models import User

# Create your models here.
class NoticeBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notices_uploaded', default=1)

    def __str__(self) -> str:
        return self.title