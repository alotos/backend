from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
# Create your models here.


class MainPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = RichTextUploadingField(blank=True, verbose_name="Содержимое статьи", default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

class ContactsPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Должность")
    text = RichTextUploadingField(blank=True, verbose_name="О сотруднике", default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Страница контактов'
        verbose_name_plural = 'Страница контактов'


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="Слайд")
    image = models.ImageField(upload_to='slides/%Y/%m/%d/', blank=True, verbose_name="Слайд")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title