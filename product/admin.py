from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created_on"]
    list_filter = ["created_on"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "weight", "price", "location", "created_on"]
    list_filter = ["created_on"]
