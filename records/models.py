from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMIN = 1
    HR = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (HR, 'Hr'),
        (EMPLOYEE, 'Employee')
    )
    
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(unique=True)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    # Add custom fields here, if needed

    def __str__(self):
        return self.username



class Record(models.Model):
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    internal_links = models.CharField(max_length=255, blank=True, null=True)
    external_links = models.CharField(max_length=255,  blank=True, null=True)

    def __str__(self):
        return f"{self.order}: {self.name}"
    



