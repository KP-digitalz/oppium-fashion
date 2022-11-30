import pytest
from decouple import config
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Returns admin user
    """
    return django_user_model.objects.create_superuser(
        config("SELENIUM_USERNAME", "SELENIUM_EMAIL", "SELENIUM_PWD")
    )


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load database data fixtures
    """

    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
