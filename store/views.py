from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from store.models import Category, Product
from store.serializers import CategorySerializers, ProductSerializers

# Create your views here.


class CategoryView(ModelViewSet):
    """Категории"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductView(ModelViewSet):
    """Категории"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

def store(request):
    return render(request, 'store/store.html')