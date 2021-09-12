from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from django.forms.models import model_to_dict


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
    """
    Function to alter a product amount in
    the basket, add or remove ect.
    """
    basket = request.session.get("basket", [])
    product = get_object_or_404(Product, pk=product_pk)

    if add:
        messages.success(request, f'Added { product.name }')
        if find_product(basket, product_pk) is not False:
            basket[find_product(basket, product_pk)]["quantity"] += 1
        else:
            basket.append({
                "pk": product_pk,
                "quantity": 1,
                "product": model_to_dict(product, exclude=["price", "rating", "image"])
            })
            basket[len(basket)-1]["product"]["price"] = float(product.price)
            basket[len(basket)-1]["product"]["rating"] = float(product.rating)
            basket[len(basket)-1]["product"]["image"] = str(product.image)
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
    """
    Quick function to find products within the basket
    as I have altered the way on which the basket
    is accessed the basket is actual a list, dictionary
    combi, whilst it would be better to use a dictionary
    I used this combi to help with production as this works
    equally as well as it would if the basket was just a
    dictionary
    """

    for i in range(0, len(dic)):
        if dic[i]["pk"] == pk:
            return i
    return False
