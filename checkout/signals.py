from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order_Items


@receiver(post_save, sender=Order_Items)
def update_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=Order_Items)
def update_save(sender, instance, **kwargs):
    instance.order.update_total()
