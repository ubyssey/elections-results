from django.db import models

class Race(models.Model):
    slug = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    results = models.CharField(max_length=200, null=True, blank=True)
    up_next = models.BooleanField()
    completed = models.BooleanField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name