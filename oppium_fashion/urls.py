from django.urls import path
from .views.index_views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="IndexView"),
]

app_name = "oppium_fashion"
