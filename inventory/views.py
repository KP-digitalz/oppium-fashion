from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryList(APIView):
    """
    Returns a list of all categories
    """

    @staticmethod
    def get(request: object) -> object:
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductList(APIView):
    """
    Returns a list of all products
    """

    @staticmethod
    def get(request: object) -> object:
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
