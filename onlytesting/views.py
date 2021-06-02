from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from onlytesting.models import Image
from onlytesting.serializers import ImageSerializers

# Create your views here.


class ImageView(ModelViewSet):
    """Категории"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializers

