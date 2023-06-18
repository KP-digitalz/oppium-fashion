from rest_framework.serializers import ModelSerializer

from inventory.models.product import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = False
