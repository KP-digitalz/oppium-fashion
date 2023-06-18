from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductAttribute(models.Model):
    """
    Product attribute table
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Product attribute name"),
        help_text=_("format: required, unique, max-255"),
    )

    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product attribute description"),
        help_text=_("format: required"),
    )

    def __str__(self):
        return self.name
