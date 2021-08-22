from django.shortcuts import render, redirect


def view_basket(request):
    """ This returns the index page """

    basket = request.session.get("basket", {})

    if "add" in request.POST:
        alter_product(request, True, request.POST["add"])
    elif "remove" in request.POST:
        if request.POST["remove"] in basket:
            alter_product(
                request, False, request.POST["remove"])
        else:
            redirect("basket/")

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
