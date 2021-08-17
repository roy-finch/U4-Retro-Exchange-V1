from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product

# Create your views here.
consoles = ["No Specific Console", "Nintendo 64", "NES", "SNES"]
categories = ["All", "Consoles", "Games", "Accessories", "Bundles"]


def all_products(request):
    """ This will display just the all products """

    products = Product.objects.all()

    if request.GET:
        query = [request.GET["c"], request.GET["q"], request.GET["f"]]
        if not query:
            return redirect("home")
        ids = [consoles.index(query[0]), categories.index(query[1])]

        if query[0] == "No Specific Console":
            queries = Q(category=ids[1])
        elif query[1] == "All":
            queries = Q(console=ids[0])
        else:
            queries = Q(console=ids[0]) & Q(category=ids[1])

        if query[0] != "No Specific Console" or query[1] != "All":
            products = products.filter(queries)
        else:
            products = products

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_pk):
    """ This will display the page of the item that has been selected."""

    products = get_object_or_404(Product, pk=int(product_pk))

    context = {
        "products": products,
    }

    return render(request, "products/product.html", context)