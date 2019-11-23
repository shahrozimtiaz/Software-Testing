from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.TextField(default=None)
    post = models.TextField(default=None)
    timeStamp = models.DateTimeField(auto_now=True)