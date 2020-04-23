from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=100)
    music_title=models.CharField(max_length=30)
    rank=models.IntegerField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review=models.ForeignKey(Review, on_delete=models.CASCADE)
    content=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
