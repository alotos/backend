from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from content.models import MainPage, ContactsPage, Slider
from content.serializers import MainPageSerializers, ContactsPageSerializers, SliderSerializers

# Create your views here.


class MainPageView(ModelViewSet):
    """Главная страница"""
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializers


class ContactsPageView(ModelViewSet):
    """Контакты"""
    queryset = ContactsPage.objects.all()
    serializer_class = ContactsPageSerializers

class SliderView(ModelViewSet):
    """Слайдер"""
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers

def content(request):
    return render(request, 'content/content.html')