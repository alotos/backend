from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from store.models import Category, Product


class CategorySerializers(ModelSerializer):
    """Сериализация категории товаров"""

    class Meta:
        model = Category
        fields = ['name1', 'name2', 'value']

class ProductSerializers(ModelSerializer):
    category = serializers.CharField(source='category.name')
    """Сериализация продукта"""

    class Meta:
        model = Product
        fields = ['id', 'article', 'category', 'name', 'image', 'description', 'price', 'stock', 'available']


