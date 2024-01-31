from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Restaurant(models.Model):
    title = models.CharField(max_length=495)
    address = models.CharField(max_length=495)
    city = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.category)


def validate_positive(value):
    if value < 1:
        raise ValidationError("The Price must be greater than 0")


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=998)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    quantity = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="Product Images", null=True, blank=True, default="default.jpg"
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
