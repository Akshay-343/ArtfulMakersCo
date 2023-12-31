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


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artisan = models.ForeignKey('Artisan', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
