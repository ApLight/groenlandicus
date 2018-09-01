from django.db import models

class Quiz(models.Model):
    problem = models.CharField(max_length=200)
    answer = models.BooleanField()
    explanation = models.CharField(max_length=200)
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return "%d: %s" % (self.id, self.problem)

