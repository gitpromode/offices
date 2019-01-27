from django.db import models

# Create your models here.

class PageCounter(models.Model):
    total_count = models.IntegerField(default=0)