from django.db import models


class Basket(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
