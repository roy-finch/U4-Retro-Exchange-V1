from django.conf import settings


def basket_contents(request):

    total = 0
    product_count = 0
    basket = request.session.get("basket", [])

    for x in range(0, len(basket)):
        total += basket[x]["price"] * int(basket[x]["quantity"])
        product_count += basket[x]["quantity"]
        shipping = total*round(float(
                    settings.STANDARD_DELIVERY_PERCENTAGE/100), 2)
        basket[x] = {
                "pk": basket[x]["pk"],
                "quantity": basket[x]["quantity"],
                "name": basket[x]["name"],
                "image": basket[x]["image"],
                "price": basket[x]["price"],
                "description": basket[x]["description"],
                "shipping": shipping,
                "total_cost": basket[x]["quantity"]*(
                    shipping+basket[x]["price"]),
            }

    grand_total = total+round(
        total * settings.STANDARD_DELIVERY_PERCENTAGE/100, 2)

    context = {
        "basket_contents": basket,
        "total": total,
        "grand_total": grand_total,
        "product_count": product_count,
    }

    return context
