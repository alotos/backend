from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from content.models import MainPage, ContactsPage, Slider


class MainPageSerializers(ModelSerializer):
    """Сериализация главной страницы"""

    class Meta:
        model = MainPage
        fields = ['title', 'text']

SEARCH_PATTERN = 'href=\\"/media/ckeditor/'
SITE_DOMAIN = "http://127.0.0.1:8000"
REPLACE_WITH = 'href=\\"%s/media/ckeditor/' % SITE_DOMAIN
class ContactsPageSerializers(ModelSerializer):
    """Сериализация страницы контактов"""

    class Meta:
        model = ContactsPage
        fields = ['title', 'text']












class SliderSerializers(ModelSerializer):
    """Сериализация слайдера"""

    class Meta:
        model = Slider
        fields = ['image']
