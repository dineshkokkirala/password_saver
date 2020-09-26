from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Passwords(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    websitename = models.CharField(max_length=200)
    websiteurl = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mainone = models.CharField(max_length=200, blank=True)
    save_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.websitename
