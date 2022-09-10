from django.contrib import admin

from .models import Car, Consumable


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Admin class for car model."""

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "user",
                ),
            },
        ),
    )
    list_display = ["user", "title"]
    search_fields = ["user", "title"]


@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    """Admin class for consumable model."""

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "replacement_mileage",
                    "car",
                ),
            },
        ),
    )
    list_display = ["car", "title"]
    search_fields = ["car", "title"]
