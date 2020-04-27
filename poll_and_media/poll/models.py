from django.db import models

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=40)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    image = models.ImageField()

class Comment(models.Model):
    vote=models.ForeignKey(Vote,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pick = models.IntegerField()