from django.db import models

class createAccount(models.Model):
    username = models.CharField(max_length = 255 , unique = True)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    isActive = models.BooleanField(default = True)
    isStaff = models.BooleanField(default = False)
    surname = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    birthDate = models.DateTimeField(max_length = 255)
    paymentMethod = models.CharField(max_length = 255)