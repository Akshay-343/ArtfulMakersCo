from django.db import models
from django.contrib.auth.models import User


class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='artisans/profile_pictures/', blank=True, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='customers/profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
