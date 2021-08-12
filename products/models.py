from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name 

    def get_friendly_name(self):
        return self.display_name


class Product(models.Model):