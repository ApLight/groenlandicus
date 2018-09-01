from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    kakaoID = models.CharField(max_length=20)
    level = models.PositiveIntegerField(default=0)
    exp = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.kakaoID
