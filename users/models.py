from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    user_bio = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Use the custom manager

    def __str__(self):
        return self.email

