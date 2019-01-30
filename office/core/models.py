from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class PageCounter(models.Model):
    total_count = models.IntegerField(default=0)


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField(blank=True)