from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConsumablesConfig(AppConfig):
    """Config class for consumables app."""

    name = "smcp.consumables"
    verbose_name = _("Consumables")
