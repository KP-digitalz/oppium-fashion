from django.contrib import admin
from django.urls import include, path

import inventory.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(inventory.urls, namespace="inventory")),
]


app_name = "oppium_fashion"
