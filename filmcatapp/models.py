from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    seen =
    date_seen = model.DateTimeField(default=timezone.now)
