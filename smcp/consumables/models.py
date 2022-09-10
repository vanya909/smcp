from django.contrib.postgres.fields import ArrayField, CICharField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    """Model for user's car."""

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    user = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        related_name="cars",
        verbose_name=_("Car owner"),
    )
    title = CICharField(
        max_length=255,
        verbose_name=_("Car title"),
    )

    def __str__(self):
        return f"<{self.pk}> {self.title}, User: {self.user.email}"


class Consumable(models.Model):
    """Model for each consumable of car."""

    class Meta:
        verbose_name = _("Consumable")
        verbose_name_plural = _("Consumables")

    car = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE,
        related_name="consumables",
        verbose_name=_("Car owner"),
    )
    title = CICharField(
        max_length=255,
        verbose_name=_("Consumable title"),
    )
    replacement_mileage = ArrayField(
        base_field=models.PositiveIntegerField(),
        verbose_name=_("List of mileages when consumable was replaced"),
    )

    def __str__(self):
        return f"<{self.pk}> {self.title}, Car: {self.car.title}"
