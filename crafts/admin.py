from django.contrib import admin
from .models import Artisan, Customer, Product

# Register your models with the admin site
admin.site.register(Product)
admin.site.register(Artisan)
admin.site.register(Customer)
