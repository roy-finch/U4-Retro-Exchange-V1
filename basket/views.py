from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ This returns the index page """

    if "add" in request.POST:
        alter_product(request, True, request.POST["add"])
        return redirect("/basket/")
    elif "remove" in request.POST:
        alter_product(
                request, False, request.POST["remove"])
        return redirect("/basket/")

    return render(request, "basket/basket.html")


def alter_product(request, add, product_pk):

    basket = request.session.get("basket", {})
    product = get_object_or_404(Product, pk=product_pk)

    if add:
        messages.success(request, f'Added { product.name }')
        if find_product(basket, product_pk) is not False:
            basket[find_product(basket, product_pk)]["quantity"] += 1
        else:
            basket[str(len(basket))] = {
                "pk": product_pk,
                "quantity": 1,
                "name": product.name,
                "image": str(product.image),
                "price": float(product.price),
                "description": product.description,
            }
    else:
        messages.success(request, f'Removed { product.name }')
        if find_product(basket, product_pk) is not False and basket[
                find_product(basket, product_pk)]["quantity"] > 1:
            basket[find_product(basket, product_pk)]["quantity"] -= 1
        elif find_product(basket, product_pk) is not False and basket[
                find_product(basket, product_pk)]["quantity"] == 1:
            del basket[find_product(basket, product_pk)]

    request.session["basket"] = basket
    return basket


def find_product(dic, pk):
    for i in range(0, len(dic)):
        if dic[str(i)]["pk"] == pk:
            return str(i)
    return False
