from django.db import models

# Create your models here.
class NoticeBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title