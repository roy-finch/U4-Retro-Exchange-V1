from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ This will display just the all products """

    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)


def products_detail(request, product_id):
    """ This will display the page of the item that has been selected."""

    products = get_object_or_404(Product, pk=int(product_id))

    context = {
        "products": products,
    }

    return render(request, "products/product.html", context)