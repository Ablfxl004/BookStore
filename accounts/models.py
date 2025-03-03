from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)
    nat_id = models.CharField(max_length=10, blank=True, null=False)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
