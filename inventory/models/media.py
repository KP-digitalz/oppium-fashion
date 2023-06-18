from django.db import models
from django.utils.translation import gettext_lazy as _

from .product_inventory import ProductInventory


class Media(models.Model):
    """
    The product image table.
    """

    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media_product_inventory",
    )

    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product image"),
        upload_to="images/",
        default="images/default.png",
        help_text=_("format: required, default-default.png"),
    )

    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Alternative text per image for SEO"),
        help_text=_("format: required, max-255"),
    )

    is_feature = models.BooleanField(
        default=True,
        verbose_name=_("Product default image"),
        help_text=_("format: default=false, true=default image"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Product visibility"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Product image")
        verbose_name_plural = _("Product images")
