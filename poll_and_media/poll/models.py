from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=40)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    image = models.ImageField()
    image_thumbnail = ProcessedImageField(
                          blank=True,
                          processors=[ResizeToFill(100, 50)],
                          format='JPEG',
                          options={'quality': 60})

class Comment(models.Model):
    vote=models.ForeignKey(Vote,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pick = models.IntegerField()