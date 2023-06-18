from django.db import models

from .product_attribute_value import ProductAttributeValue
from .product_inventory import ProductInventory


class ProductAttributeValues(models.Model):
    """
    Product attribute values link table
    """

    attribute_values = models.ForeignKey(
        ProductAttributeValue,
        related_name="attributevaluess",
        on_delete=models.PROTECT,
    )

    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="productattributevaluess",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("attribute_values", "product_inventory"),)
