from django import forms
from django.contrib.auth.models import User
from .models import Product, Review

class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = []

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'type', 'image', 'product_desc']

class ProductFormAdmin(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'type', 'image', 'height_field', 'width_field', 'product_desc']

class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Review
        fields = ['review_text']

class ReviewFormAdmin(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Review
        fields = ['product', 'user', 'score', 'flag', 'review_text']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']