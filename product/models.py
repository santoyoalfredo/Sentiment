from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.db import models
from django import forms

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=100)
    product_image = models.CharField(max_length=1000)
    product_desc = models.TextField(max_length=2000)
    average_score = models.DecimalField(max_digits=8, decimal_places=1, default=0)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1)
    score = models.DecimalField(max_digits=8, decimal_places=1)
    review_text = models.TextField(max_length=2000)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)