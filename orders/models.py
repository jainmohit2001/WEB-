from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart
from users.models import Address


User = get_user_model()

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart, related_name="order", on_delete=models.CASCADE)
    # address = models.ForeignKey(Address, related_name="order_address", on_delete=models.CASCADE)
    shipping_total = models.DecimalField(max_digits=10, decimal_places=2, default=5.99)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.order_id
