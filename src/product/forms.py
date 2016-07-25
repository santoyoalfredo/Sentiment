from django import forms
from django.contrib.auth.models import User
from .models import Product, Review

# Form for deleting a review
class DeleteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = []

# Form for deleting a product
class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = []

# Form for the Product model
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'type', 'image', 'product_desc']

# Form for adding a product through the Django Admin site
class ProductFormAdmin(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'type', 'image', 'height_field', 'width_field', 'product_desc']

# Form for flagging a review
class FlagReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = []

# Form for the Review model
class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Review
        fields = ['review_text']

# Form for adding a review in the Django Admin site
class ReviewFormAdmin(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Review
        fields = ['product', 'user', 'score', 'flag', 'review_text']

# Form for the User model
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']