from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    photo = models.ImageField(default="avatars/", null=True, blank=True)

    REQUIRED_FIELDS = [] # We removed default extra email field

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = "Accounts"