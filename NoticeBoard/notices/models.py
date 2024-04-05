from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   
    
    def __str__(self) -> str:
        return self.title