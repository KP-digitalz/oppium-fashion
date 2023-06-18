from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    """
    Inventory Category table implemented with MPTT
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Category name"),
        help_text=_("format: required, max-100"),
    )

    slug = models.SlugField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Category safe link"),
        help_text=_("format: required, letters, numbers, underscore or hyphens"),
    )

    is_active: bool = models.BooleanField(default=False)

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Parent of category"),
        help_text=_("format: not required"),
    )

    class MPPTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self) -> str:
        return self.name
