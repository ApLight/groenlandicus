from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    kakaoID = models.CharField(max_length=20)
    level = models.PositiveIntegerField(default=0)
    exp = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.kakaoID

    def feed(self, exp):
        self.exp = self.exp + int(exp)
        if self.exp >= 100:
            self.level = self.level + 1
            self.exp = self.exp - 100
        return self
