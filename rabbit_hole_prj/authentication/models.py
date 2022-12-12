from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below

# Fields already in the model are:
#   id:             int(pk)
#   password:       char(128)
#   last_login:     datetime(6)
#   is_superuser:   tinyint(1) - boolean    (ADMIN ONLY)
#   username:       char(150)
#   first_name:     char(150)
#   last_name:      char(150)
#   email:          char(254)
#   is_staff:       tinyint(1) - boolean
#   is_active:      tinyint(1) - boolean
#   date_joined:    datetime(6)


class User(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    plan = models.CharField(max_length=1, default="B")  # B=Basic/Free plan

    def __str__(self):
        if (self.nick_name != "") & (self.nick_name != None):
            return self.nick_name
        elif(self.first_name != ""):
            return self.first_name + " " + self.last_name
        else:
            return self.username
