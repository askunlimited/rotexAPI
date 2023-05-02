from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Product(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    weight = models.FloatField(default=0, blank=True)
    price = models.FloatField(default=0, blank=True)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product_category",
        related_query_name="product_category",
        null=True,
        blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=upload_to, default="", null=True, blank=True)
