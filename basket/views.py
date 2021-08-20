from django.shortcuts import render


def view_basket(request):
    """ This returns the index page """

    if "add" in request.GET:
        alter_product(request, True, request.GET["add"])
    elif "remove" in request.GET:
        alter_product(
            request, False, request.GET["remove"])

    return render(request, "basket/basket.html")


def alter_product(request, add, product_pk):

    basket = request.session.get("basket", {})

    if add:
        if product_pk in list(basket.keys()):
            basket[product_pk] += 1
        else:
            basket[product_pk] = 1
    else:
        if product_pk in list(basket.keys()) and basket[product_pk] > 1:
            basket[product_pk] -= 1
        else:
            basket.pop(product_pk)

    request.session["basket"] = basket
    return basket
