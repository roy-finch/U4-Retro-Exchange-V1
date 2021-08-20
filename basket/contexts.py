from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get("basket", {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity

    grand_total = total*settings.STANDARD_DELIVERY_PERCENTAGE

    context = {
        "basket_contents": basket_items,
        "total": total,
        "grand_total": grand_total,
        "product_count": product_count,
    }

    return context
