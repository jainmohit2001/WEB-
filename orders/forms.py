from django import forms
from users.models import Address


ADDRESS_TYPE = (
    ("H", "Home Address"),
    ("W", "Work/Office Address")
)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['zip', 'house_no', 'area', 'city', 'state', 'landmark', 'name', 'mobile_no', 'alternate_no',
                  'address_type']


