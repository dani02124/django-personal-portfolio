from django.db import models
from django.utils import timezone


class BlogProject(models.Model):
    titel = models.CharField(max_length=100)
    description = models.TextField(max_length=550)
    date = models.DateTimeField(default= timezone.now,null=True , blank=True)

    def __str__(self):
        return self.titel
