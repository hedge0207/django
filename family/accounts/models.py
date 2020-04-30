from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class MyUser(AbstractUser):
    family_followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='family_followings')