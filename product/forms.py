from django import forms
from django.contrib.auth.models import User
from .models import Product, Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Review
        fields = ['review_text']

class ReviewFormAdmin(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Review
        fields = ['product', 'user', 'score', 'flag', 'review_text']

class ProductForm(forms.ModelForm):
    product_image = forms.ImageField(widget=forms.FileInput)
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'type', 'product_image', 'product_desc']