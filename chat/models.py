from django.db import models
# from django.apps.registry import apps

# Product = apps.get_model('product', 'Product')
from product.models import Product

class Conversations(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=16)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject




