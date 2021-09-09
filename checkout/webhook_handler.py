from django.http import HttpResponse


class Stripe_WH_Handler:
    """ This will deal with webhooks for stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(content=f"Webhook recieved: {event['type']}",
                            status=200)

    def handle_succeeded_payment(self, event):
        intent = event.data.object
        print(intent)
        return HttpResponse(content=f"Webhook recieved: {event['type']}",
                            status=200)

    def handle_failed_payment(self, event):
        return HttpResponse(content=f"Webhook recieved: {event['type']}",
                            status=200)
