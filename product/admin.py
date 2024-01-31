from django.contrib import admin
from .models import Restaurant, Category, Product

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "address", "city", "created_at"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "category"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "quantity",
        "price",
        "image",
        "category",
        "restaurant",
    ]