from django.contrib import admin
from .models import Product, Category, Console

# Register your models here.


class ProductAdmin():
    list_display = {
        "sku",
        "name",
        "price",
        "console",
        "category",
        "rating",
        "image"
    }


class CategoryAdmin():
    list_display = {
        "name",
        "display_name",
    }


class ConsoleAdmin():
    list_display = {
        "name",
        "display_name",
    }


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Console)
