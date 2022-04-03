from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True, default='hello')
    year = models.PositiveIntegerField(default=2)
    branch = models.CharField(max_length= 10, default='ECE' )