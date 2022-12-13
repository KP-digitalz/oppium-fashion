import oppium_fashion.urls
import inventory.urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("", include(oppium_fashion.urls, namespace="oppium_fashion")),
    path("api/", include(inventory.urls, namespace="inventory")),
]


app_name = "oppium_fashion"
