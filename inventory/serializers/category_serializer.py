from rest_framework.serializers import ModelSerializer

from inventory.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]
        read_only = True
