from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    role = models.CharField(max_length=20, choices=(('admin', 'Admin'), ('user', 'User')))
    image_path = models.CharField(max_length=255, null=True)