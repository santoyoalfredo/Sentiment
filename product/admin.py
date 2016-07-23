from django.contrib import admin
from .forms import ProductForm, ReviewForm, ReviewFormAdmin
from .models import Product, Review

class ProductAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name", "price", "type", "average_score"]
	form = ProductForm

class ReviewAdmin(admin.ModelAdmin):
	list_display = ["__str__", "product", "user", "score", "flag"]
	form = ReviewFormAdmin

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)