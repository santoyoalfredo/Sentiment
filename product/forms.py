from django import forms
from django.contrib.auth.models import User

from .models import Review

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