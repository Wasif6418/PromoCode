from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from autoslug import AutoSlugField


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suggestions = models.ManyToManyField('self', blank=True, symmetrical=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.product_name






"""
    def get_suggestions(self, product):
        # Retrieve the related suggestions and serialize them
        suggestions = ProductSerializer(product.suggestions.all(), many=True).data
        return suggestions



from django.db import models


class Product(models.Model):
    Productname = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Productname


class Suggestion(models.Model):
    product = models.ForeignKey(Product, related_name='suggestions', on_delete=models.CASCADE)
    suggestion_name =  models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.suggestion_name
"""
