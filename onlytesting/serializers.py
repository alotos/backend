from rest_framework.serializers import ModelSerializer

from onlytesting.models import Image



class ImageSerializers(ModelSerializer):
    """Сериализация продукта"""

    class Meta:
        model = Image
        fields = ['id', 'name', 'image']


