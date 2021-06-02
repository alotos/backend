# Generated by Django 3.2 on 2021-05-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Изображение товара')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ['name'],
                'index_together': {('id',)},
            },
        ),
    ]
