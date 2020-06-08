from django.db import models
from faker import Faker

f = Faker()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    @classmethod
    def dummy(cls,n):
        for _ in range(n):
            cls.objects.create(
                title=f.name(),
                content=f.text()
            )

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.CharField(max_length=150)