import pytest
from django.db import IntegrityError
from inventory.models import ProductInventory


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(db, category_factory, slug, is_active):
    result = category_factory.create(slug=slug, is_active=is_active)
    # assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


def test_inventory_db_product_insert_data(db, product_factory, category_factory):
    new_product = product_factory.create(category=(1, 2, 3, 4, 5))

    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
    assert result_product_category == 5


def test_inventory_db_product_inventory_insert_data(db, product_inventory_factory):
    new_product = product_inventory_factory.create(
        sku="123456789",
        upc="123456789",
        product_type__name="new_name",
        product__web_id="123456789",
        brand__name="new_name",
    )

    assert new_product.sku == "123456789"
    assert new_product.upc == "123456789"
    assert new_product.product_type.name == "new_name"
    assert new_product.product.web_id == "123456789"
    assert new_product.brand.name == "new_name"
    assert new_product.is_active == 0
    assert new_product.retail_price == 97.00
    assert new_product.store_price == 92.00
    assert new_product.sale_price == 46.00
    assert new_product.weight == 987


def test_inventory_db_product_type_insert_data(db, product_type_factory):
    new_type = product_type_factory.create(name="demo_type")
    assert new_type.name == "demo_type"


def test_inventory_db_product_type_uniqueness_integrity(db, product_type_factory):
    product_type_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="not_unique")


def test_inventory_db_brand_insert_data(db, brand_factory):
    new_brand = brand_factory.create(name="demo_brand")
    assert new_brand.name == "demo_brand"


def test_inventory_db_brand_uniqueness_integrity(db, brand_factory):
    brand_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        brand_factory.create(name="not_unique")


def test_inventory_db_media_insert_data(db, media_factory):
    new_media = media_factory.create(product_inventory__sku="123456789")
    assert new_media.product_inventory.sku == "123456789"
    assert new_media.image == "images/default.png"
    assert new_media.alt_text == "a default image solid color"
    assert new_media.is_feature == 1


def test_inventory_db_stock_insert_data(db, stock_factory):
    new_stock = stock_factory.create(product_inventory__sku="123456789")
    assert new_stock.product_inventory.sku == "123456789"
    assert new_stock.units == 2
    assert new_stock.units_sold == 100


def test_inventory_db_product_attribute_insert_data(db, product_attribute_factory):
    new_attribute = product_attribute_factory.create()
    assert new_attribute.name == "attribute_name_0"
    assert new_attribute.description == "description_0"


def test_inventory_db_product_attribute_uniqueness_integrity(
    db, product_attribute_factory
):
    product_attribute_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name="not_unique")


def test_inventory_db_product_attribute_value_data(db, product_attribute_value_factory):
    new_attribute_value = product_attribute_value_factory.create(
        attribute_value="new_value", product_attribute__name="new_value"
    )

    assert new_attribute_value.attribute_value == "new_value"
    assert new_attribute_value.product_attribute.name == "new_value"


def test_inventory_db_insert_inventory_product_values(
    db, product_with_attribute_values_factory
):
    product_with_attribute_values_factory.create(sku="123456789")
    result = ProductInventory.objects.get(sku="123456789")
    counter = result.attribute_values.all().count()

    assert counter == 2
