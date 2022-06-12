from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below


class User(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
