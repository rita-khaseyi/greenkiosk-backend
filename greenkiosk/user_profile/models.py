from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True, default='')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.username
