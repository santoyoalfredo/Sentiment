from django.contrib import admin
from .models import Product, Review

# Allows for the table Album to be modifiable in the admin interface of the site
admin.site.register(Product)
admin.site.register(Review)
