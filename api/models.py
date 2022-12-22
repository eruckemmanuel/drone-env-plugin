from django.db import models


class EnvVariable(models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField(default='', blank=True)
    mask = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
