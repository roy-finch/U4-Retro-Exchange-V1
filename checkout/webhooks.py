from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import Stripe_WH_Handler

import stripe
import json


@require_POST
@csrf_exempt
def webhook(request):
    wh_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # if event.type == "payment_intent.succeeded":
    #     payment_intent = event.data.object
    #     print("PaymentIntent successful")
    # elif event.type == "payment_method.attached":
    #     payment_method = event.data.object
    #     print("PaymentMethod attached to customer!")
    # else:
    #     return HttpResponse(status=400)

    return HttpResponse(status=200)
