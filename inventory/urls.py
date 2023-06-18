from django.urls import path

from .views import CategoryList, ProductList

urlpatterns = [
    path(
        "inventory/category/all/",
        CategoryList.as_view(),
        name="category-list-view",
    ),
    path(
        "inventory/product/all/",
        ProductList.as_view(),
        name="product-list-view",
    ),
]

app_name = "inventory"
