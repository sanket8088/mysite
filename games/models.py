from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)



class Courses(models.Model):
    school = models.ForeignKey(School, null=True, related_name='school_name', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    strength = models.IntegerField()