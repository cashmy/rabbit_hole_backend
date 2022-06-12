from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below


class User(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username + ": " + self.first_name + " " + self.last_name
