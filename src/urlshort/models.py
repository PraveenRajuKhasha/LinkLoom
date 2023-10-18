from django.db import models

# Create your models here.

class ShortURL(models.Model):
    original_url = models.URLField(max_length=900)
    short_url = models.CharField(max_length=90)
    time_date_created = models.DateTimeField()

    def __str__(self):
        return self.original_url