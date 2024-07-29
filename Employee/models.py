from django.db import models


class Employee(models.Model):
    firstName = models.CharField(max_length=255,blank=True)   
    lastName = models.CharField(max_length=255,blank=True)
    emailId = models.EmailField(blank=True)
    