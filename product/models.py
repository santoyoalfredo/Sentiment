from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django import forms

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=100)
    product_image = models.CharField(max_length=1000)
    product_desc = models.TextField(max_length=2000)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' - ' + str(self.price)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1)
    score = models.DecimalField(max_digits=8, decimal_places=1)
    review_text = models.TextField(max_length=2000)

    def __str__(self):
        return 'Review for ' + str(self.product) + ': ' + self.review_text






