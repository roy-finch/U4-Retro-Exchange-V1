from django.shortcuts import render


def view_basket(request):
    """ This returns the index page """

    return render(request, "basket/basket.html")


def add_product(request, product_pk):

    basket = request.session.get("basket", {})

    if product_pk in list(basket.keys()):
        basket[product_pk] += 1
    else:
        basket[product_pk] = 1

    request.session["basket"] = basket
    return basket
