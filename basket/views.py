from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ This returns the index page """

    basket = request.session.get("basket", {})

    if "add" in request.POST:
        alter_product(request, True, request.POST["add"])
        return redirect("/basket/")
    elif "remove" in request.POST:
        if request.POST["remove"] in basket:
            alter_product(
                request, False, request.POST["remove"])
            return redirect("/basket/")
        else:
            redirect("basket/")

    return render(request, "basket/basket.html")


def alter_product(request, add, product_pk):

    basket = request.session.get("basket", {})
    product = Product.objects.get(pk=product_pk)

    if add:
        messages.success(request, f'Added { product.name }')
        if product_pk in list(basket.keys()):
            basket[product_pk] += 1
        else:
            basket[product_pk] = 1
    else:
        messages.success(request, f'Removed { product.name }')
        if product_pk in list(basket.keys()) and basket[product_pk] > 1:
            basket[product_pk] -= 1
        else:
            basket.pop(product_pk)

    request.session["basket"] = basket
    return basket
