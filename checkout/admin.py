from django.contrib import admin
from .models import Order, Order_Items


class OrderItemsAdmin(admin.TabularInline):
    model = Order_Items
    readonly_fields = ("indiv_item_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsAdmin,)

    readonly_fields = (
        "order_number", "date", "delivery_cost", "order_total", "grand_total",)

    fields = ("order_number", "user_profile", "date", "full_name", "email", "phone_number", "country", "postcode", "town_r_city", "street_add_line1", "street_add_line2", "county", "delivery_cost", "order_total", "grand_total",)

    list_display = ("order_number", "date", "full_name", "delivery_cost", "order_total", "grand_total",)

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
