from django.contrib.auth.models import AbstractUser
from django.db import models
from forosh.models import*

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    # advertisment = models.ForeignKey('Advertisment', on_delete=models.CASCADE,)

    def __str__(self):
        return self.email
