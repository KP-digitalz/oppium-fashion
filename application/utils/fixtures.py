import pytest
from decouple import config
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Returns admin user
    """
    return django_user_model.objects.create_superuser(
        config("FIXTURE_USER"), config("FIXTURE_EMAIL"), config("FIXTURE_PASSWORD")
    )


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load database data fixtures
    """

    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_product_type_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_product_inventory_fixture.json")
        call_command("loaddata", "db_media_fixture.json")
        call_command("loaddata", "db_stock_fixture.json")
        call_command("loaddata", "db_product_attribute_fixture.json")
        call_command("loaddata", "db_product_attribute_value_fixture.json")
        call_command("loaddata", "db_product_attribute_values_fixture.json")
