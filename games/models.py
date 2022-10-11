from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)