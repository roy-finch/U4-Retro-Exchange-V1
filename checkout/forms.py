from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("full_name", "email", "phone_number", "street_add_line1", "street_add_line2", "town_r_city", "postcode", "country", "county",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {"full_name": "Full Name", "email": "Email Address", "phone_number": "Phone Number", "country": "Country", "county": "County", "street_add_line1": "First Line of your Address", "street_add_line2": "Second Line of your Address", "town_r_city": "Town / City", "postcode": "Postal Code"}

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]}"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False
