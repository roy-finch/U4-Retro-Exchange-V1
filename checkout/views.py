from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get("basket", [])
    if not basket:
        messages.error(request, "Theres nothing in your basket the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51JWGrqC13WIsUQb1Obfkw8vLy1FvRL96cVBk7zvAeHRZYLAhb5dyLOrDKaqpHXC8edNOKukk1HzpNlvP6tUiNp8g00N7Udn8hX",
        "client_key": "test client key",
    }

    return render(request, template, context)
