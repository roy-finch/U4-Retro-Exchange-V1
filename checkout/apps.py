from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Import the signals and corresponding files
    to perform stripe webhooks.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
