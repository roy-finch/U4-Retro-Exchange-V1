from django.conf import settings
from decimal import Decimal


def basket_contents(request):

    total = 0
    product_count = 0
    basket = request.session.get("basket", {})

    for x in range(0, len(basket)):
        total += basket[str(x)]["price"] * int(basket[str(x)]["quantity"])
        product_count += basket[str(x)]["quantity"]
        shipping = total*Decimal(
                    settings.STANDARD_DELIVERY_PERCENTAGE/100)
        basket[str(x)].append(
            {
                "shipping": shipping,
                "total_cost": basket[str(x)]["quantity"]*(
                    shipping+basket[str(x)]["price"]),
            }
        )

    grand_total = total+(total*Decimal(
        settings.STANDARD_DELIVERY_PERCENTAGE/100))

    context = {
        "basket_contents": basket,
        "total": total,
        "grand_total": grand_total,
        "product_count": product_count,
    }

    return context
