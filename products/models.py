from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.display_name


class Console(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.display_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    console = models.ForeignKey(
        'Console', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
