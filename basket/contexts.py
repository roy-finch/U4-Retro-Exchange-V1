from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get("basket", {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price * quantity
        product_count += quantity
        shipping = round(total*Decimal(
                    settings.STANDARD_DELIVERY_PERCENTAGE/100), 2)
        basket_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "shipping": shipping,
                "total_cost": quantity*(shipping+product.price),
                "product": product,
            }
        )

    grand_total = total+(total*Decimal(
        settings.STANDARD_DELIVERY_PERCENTAGE/100))

    context = {
        "basket_contents": basket_items,
        "total": total,
        "grand_total": grand_total,
        "product_count": product_count,
    }
    print(total, grand_total)
    return context
