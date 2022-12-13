from django.urls import path
from .views import CategoryList

urlpatterns = [
    path(
        "inventory/category/all/",
        CategoryList.as_view(),
        name="category-list-view",
    ),
]

app_name = "inventory"
