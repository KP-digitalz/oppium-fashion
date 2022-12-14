# Generated by Django 4.1.3 on 2022-11-20 14:08

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, unique, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="Brand name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-100",
                        max_length=100,
                        verbose_name="Category name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscore or hyphens",
                        max_length=100,
                        verbose_name="Category safe link",
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        help_text="format: not required",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="inventory.category",
                        verbose_name="Parent of category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Category",
                "verbose_name_plural": "Product Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "web_id",
                    models.CharField(
                        help_text="format: required, unique",
                        max_length=50,
                        unique=True,
                        verbose_name="Product website ID",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        help_text="format: required, letters, numbers, underscore or hyphens",
                        max_length=110,
                        verbose_name="Product safe URL",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-110",
                        max_length=110,
                        verbose_name="Product name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="format: required", verbose_name="Product description"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        help_text="format: true = product visible",
                        verbose_name="Product visibility",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Time of publishing the product",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Last time the product has been updated at",
                    ),
                ),
                ("category", mptt.fields.TreeManyToManyField(to="inventory.category")),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, unique, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="Product attribute name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="format: required",
                        verbose_name="Product attribute description",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attribute_value",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        verbose_name="attribute value",
                    ),
                ),
                (
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_attribute",
                        to="inventory.productattribute",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttributeValues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attribute_values",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="attributevaluess",
                        to="inventory.productattributevalue",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        help_text="format: required, unique, max-20",
                        max_length=20,
                        unique=True,
                        verbose_name="Stock keeping unit",
                    ),
                ),
                (
                    "upc",
                    models.CharField(
                        help_text="format: required, unique, max-12",
                        max_length=12,
                        unique=True,
                        verbose_name="Universal product code",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        help_text="format: true = product visible",
                        verbose_name="Product visibility",
                    ),
                ),
                (
                    "retail_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="Recommended retail price",
                    ),
                ),
                (
                    "store_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="Regular store price",
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="Sale price",
                    ),
                ),
                ("weight", models.FloatField(verbose_name="Product weight")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Date sub-product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Date sub-product updated",
                    ),
                ),
                (
                    "attribute_values",
                    models.ManyToManyField(
                        related_name="product_attribute_values",
                        through="inventory.ProductAttributeValues",
                        to="inventory.productattributevalue",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="brand",
                        to="inventory.brand",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product",
                        to="inventory.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, unique, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="Type of product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_checked",
                    models.DateTimeField(
                        blank=True,
                        help_text="format: Y-m-d H:M:S, null-true, blank-true",
                        null=True,
                        verbose_name="Inventory stock check date",
                    ),
                ),
                (
                    "units",
                    models.IntegerField(
                        default=0,
                        help_text="format: required, default-0",
                        verbose_name="Units/amount of stock",
                    ),
                ),
                (
                    "units_sold",
                    models.IntegerField(
                        default=0,
                        help_text="format: required, default-0",
                        verbose_name="Units sold to date",
                    ),
                ),
                (
                    "product_inventory",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_inventory",
                        to="inventory.productinventory",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productinventory",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_type",
                to="inventory.producttype",
            ),
        ),
        migrations.AddField(
            model_name="productattributevalues",
            name="product_inventory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="productattributevaluess",
                to="inventory.productinventory",
            ),
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        help_text="format: required, default-default.png",
                        upload_to="images/",
                        verbose_name="Product image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        verbose_name="Alternative text per image for SEO",
                    ),
                ),
                (
                    "is_feature",
                    models.BooleanField(
                        default=True,
                        help_text="format: default=false, true=default image",
                        verbose_name="Product default image",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Product visibility",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="Date sub-product created",
                    ),
                ),
                (
                    "product_inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="media_product_inventory",
                        to="inventory.productinventory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product image",
                "verbose_name_plural": "Product images",
            },
        ),
        migrations.AlterUniqueTogether(
            name="productattributevalues",
            unique_together={("attribute_values", "product_inventory")},
        ),
    ]
