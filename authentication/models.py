from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    full_name = models.CharField(max_length=254)
    nick_name = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=494)
    contact = models.CharField(max_length=11)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

