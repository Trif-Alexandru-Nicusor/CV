from django.db import models
from django.utils import timezone
class createAccount(models.Model):
    username = models.CharField(max_length = 255 , unique = True)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    isActive = models.BooleanField(default = True)
    isStaff = models.BooleanField(default = False)
    joined = models.DateTimeField(default = timezone.now)
    surname = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    birthDate = models.DateField(max_length = 255 , default = '1000-10-10')
    paymentMethod = models.CharField(max_length = 255)