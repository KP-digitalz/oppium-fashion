from django.contrib import admin
from django.urls import include, path

import inventory.urls

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/", include(inventory.urls, namespace="inventory")),
]


app_name = "oppium_fashion"
