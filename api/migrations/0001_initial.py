# Generated by Django 4.1.4 on 2022-12-14 16:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfClothes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type_name', models.CharField(help_text='Тип одежды(Футболки, Шорты, Худи и т.д.)', max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=250)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Clothings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Название товара', max_length=200, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(blank=True, help_text='Описание товара', max_length=2000, verbose_name='Описание')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 1')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 3')),
                ('size_xs', models.IntegerField(help_text='Количество данного размера', null=True, verbose_name='XS')),
                ('size_s', models.IntegerField(help_text='Количество данного размера', null=True, verbose_name='S')),
                ('size_m', models.IntegerField(help_text='Количество данного размера', null=True, verbose_name='M')),
                ('size_l', models.IntegerField(help_text='Количество данного размера', null=True, verbose_name='L')),
                ('size_xl', models.IntegerField(help_text='Количество данного размера', null=True, verbose_name='XL')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.typeofclothes', verbose_name='Тип одежды')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id'],
            },
        ),
    ]
