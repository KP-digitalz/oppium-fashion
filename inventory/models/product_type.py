from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductType(models.Model):
    """
    Product type table
    """

    name: str = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Type of product"),
        help_text=_("format: required, unique, max-255"),
    )

    def __str__(self):
        return self.name
