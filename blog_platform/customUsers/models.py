from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Owner', 'Owner'),
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')
    email = models.EmailField(blank=True, null=True)

    def is_owner(self):
        return self.role == 'Owner'

    def is_admin(self):
        return self.role == 'Admin'

    def __str__(self):
        return self.username
