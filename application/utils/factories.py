import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

django.setup()

from datetime import datetime

import factory
from faker import Faker
from pytest_factoryboy import register

from inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductAttributeValues,
    ProductInventory,
    ProductType,
    Stock,
)

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name: str = factory.Sequence(lambda n: "cat_name_%d" % n)
    slug: str = fake.lexify(text="cat_slug_??????")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    web_id: str = factory.Sequence(lambda n: "web_id_%d" % n)
    slug: str = fake.lexify(text="prod_slug_??????")
    name: str = fake.lexify(text="prod_name_??????")
    description: str = fake.text()
    is_active: bool = False
    created_at: datetime = "2022-11-19 00:01:27.279092"
    updated_at: datetime = "2022-11-19 00:01:27.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name: str = factory.Sequence(lambda n: "type_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name: str = factory.Sequence(lambda n: "brand_%d" % n)


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductInventory

    sku: str = factory.Sequence(lambda n: "sku_%d" % n)
    upc: str = factory.Sequence(lambda n: "upc_%d" % n)
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    brand: str = factory.SubFactory(BrandFactory)
    is_active: bool = 0
    retail_price: float = 97.00
    store_price: float = 92.00
    sale_price: float = 46.00
    weight: float = 987.00


class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Media

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    image = "images/default.png"
    alt_text = "a default image solid color"
    is_feature = 1


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stock

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 2
    units_sold = 100


class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttribute

    name: str = factory.Sequence(lambda n: "attribute_name_%d" % n)
    description: str = factory.Sequence(lambda n: "description_%d" % n)


class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value: str = fake.lexify(text="attribute_value_??????")


class ProductAttributeValuesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttributeValues

    attribute_values = factory.SubFactory(ProductAttributeValueFactory)
    product_inventory = factory.SubFactory(ProductInventoryFactory)


class ProductWithAttributeValuesFactory(ProductInventoryFactory):
    attribute_values_1 = factory.RelatedFactory(ProductAttributeValuesFactory, factory_related_name="product_inventory")
    attribute_values_2 = factory.RelatedFactory(ProductAttributeValuesFactory, factory_related_name="product_inventory")


register(CategoryFactory)
register(ProductFactory)
register(ProductTypeFactory)
register(BrandFactory)
register(ProductInventoryFactory)
register(MediaFactory)
register(StockFactory)
register(ProductAttributeFactory)
register(ProductAttributeValueFactory)
register(ProductAttributeValuesFactory)
register(ProductWithAttributeValuesFactory)
