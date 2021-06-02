from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")


    class Meta:
        ordering = ['name']
        index_together = [
            ['id']
        ]
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name
