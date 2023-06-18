from django.db import models
from django.utils.translation import gettext_lazy as _

from .brand import Brand
from .product import Product
from .product_attribute_value import ProductAttributeValue
from .product_type import ProductType


class ProductInventory(models.Model):
    """
    Product inventory table
    """

    sku = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Stock keeping unit"),
        help_text=_("format: required, unique, max-20"),
    )

    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Universal product code"),
        help_text=_("format: required, unique, max-12"),
    )

    product_type = models.ForeignKey(ProductType, related_name="product_type", on_delete=models.PROTECT)

    product = models.ForeignKey(Product, related_name="product", on_delete=models.PROTECT)

    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.PROTECT)

    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="product_attribute_values",
        through="ProductAttributeValues",
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name=_("Product visibility"),
        help_text=_("format: true = product visible"),
    )

    retail_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Recommended retail price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
    )

    store_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Regular store price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
    )

    sale_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Sale price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
    )

    weight = models.FloatField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product weight"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date sub-product updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.product.name
