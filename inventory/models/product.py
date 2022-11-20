from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import TreeManyToManyField
from datetime import datetime
from .category import Category


class Product(models.Model):
    """
    Product details table
    """

    web_id: str = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Product website ID"),
        help_text=_("format: required, unique"),
    )

    slug: str = models.CharField(
        max_length=110,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product safe URL"),
        help_text=_("format: required, letters, numbers, underscore or hyphens"),
    )

    name: str = models.CharField(
        max_length=110,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product name"),
        help_text=_("format: required, max-110"),
    )

    description: str = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Product description"),
        help_text=_("format: required"),
    )

    is_active: bool = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default=False,
        verbose_name=_("Product visibility"),
        help_text=_("format: true = product visible"),
    )

    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Time of publishing the product"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at: datetime = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Last time the product has been updated at"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    category = TreeManyToManyField(Category)

    def __str__(self) -> str:
        return self.name
