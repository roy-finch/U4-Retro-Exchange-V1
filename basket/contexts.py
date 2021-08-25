from django.conf import settings


def basket_contents(request):

    total = 0
    product_count = 0
    basket = request.session.get("basket", {})

    for x in range(0, len(basket)):
        total += basket[str(x)]["price"] * int(basket[str(x)]["quantity"])
        product_count += basket[str(x)]["quantity"]
        shipping = total*round(float(
                    settings.STANDARD_DELIVERY_PERCENTAGE/100), 2)
        basket[str(x)] = {
                "pk": basket[str(x)]["pk"],
                "quantity": basket[str(x)]["quantity"],
                "name": basket[str(x)]["name"],
                "image": basket[str(x)]["image"],
                "price": basket[str(x)]["price"],
                "description": basket[str(x)]["description"],
                "shipping": shipping,
                "total_cost": basket[str(x)]["quantity"]*(
                    shipping+basket[str(x)]["price"]),
            }

    grand_total = total+round(
        total * settings.STANDARD_DELIVERY_PERCENTAGE/100, 2)

    context = {
        "basket_contents": basket,
        "total": total,
        "grand_total": grand_total,
        "product_count": product_count,
    }

    print(basket)

    return context
