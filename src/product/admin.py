from django.contrib import admin
from .forms import ProductForm, ReviewForm, ReviewFormAdmin
from .models import Product, Review

# Model for products in the Django Admin panel
class ProductAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name", "price", "type", "average_score"]
	form = ProductForm

# Model for reviews in the Django Admin panel
class ReviewAdmin(admin.ModelAdmin):
	list_display = ["__str__", "product", "user", "score", "flag"]
	form = ReviewFormAdmin

# Register models with the Admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)