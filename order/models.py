from django.db import models
from authentication.models import MyUser
from product.models import Product
from cart.models import Cart
from django.core.exceptions import ValidationError

# Create your models here.

STATUS_CHOICES = (
    ("1", "Ordered"),
    ("2", "Paid"),
    ("3", "Completed"),
    ("4", "Cancelled"),
)

def validate_positive(value):
    if value < 1:
        raise ValidationError("The Price must be greater than 0")

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user_address = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    quantity = models.PositiveBigIntegerField(default=1)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="1")

    def __int__(self):
        return int(self.id)
