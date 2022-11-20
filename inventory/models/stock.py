from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from .product_inventory import ProductInventory


class Stock(models.Model):
    """
    Stock information details
    """

    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )

    last_checked: datetime = models.DateTimeField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("Inventory stock check date"),
        help_text=_("format: Y-m-d H:M:S, null-true, blank-true"),
    )

    units: int = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Units/amount of stock"),
        help_text=_("format: required, default-0"),
    )

    units_sold: int = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Units sold to date"),
        help_text=_("format: required, default-0"),
    )
