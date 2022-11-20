from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    """
    Product brand table
    """

    name: str = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Brand name"),
        help_text=_("format: required, unique, max-255"),
    )
