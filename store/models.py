from django.db import models

# Модель категории
class Category(models.Model):
    name1 = models.CharField(max_length=200, blank=True, verbose_name="1 слово", default='', unique=True)
    name2 = models.CharField(max_length=200, blank=True, verbose_name="1 слово", default='')
    value = models.CharField(max_length=200, verbose_name='Значение', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.value

# Модель продукта
class Product(models.Model):
    article = models.CharField(max_length=100, db_index=True, verbose_name="Артикул", unique=True)
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
