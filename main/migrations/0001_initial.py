# Generated by Django 4.2.3 on 2023-07-03 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, verbose_name='Название бренда')),
                ('brand_description', models.TextField()),
                ('brand_slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('category_description', models.TextField()),
                ('category_slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_name', models.CharField(max_length=100)),
                ('clothes_description', models.TextField()),
                ('clothes_slug', models.SlugField(max_length=100, unique=True)),
                ('clothes_type', models.CharField(choices=[('man', 'Мужской'), ('woman', 'Женский'), ('kid', 'Детский'), ('uni', 'Универсальный')], max_length=10)),
                ('clothes_season', models.CharField(choices=[('winter', 'Зима'), ('spring', 'Весна'), ('summer', 'Лето'), ('autumn', 'Осень')], max_length=10)),
                ('clothes_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('clothes_image', models.ImageField(upload_to='clothes')),
                ('clothes_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.brand')),
                ('clothes_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Одежда',
                'verbose_name_plural': 'Одежда',
            },
        ),
        migrations.CreateModel(
            name='ClothesColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100, verbose_name='Название цвета')),
                ('color_slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Цвет одежды',
                'verbose_name_plural': 'Цвета одежды',
            },
        ),
        migrations.CreateModel(
            name='ClothesSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn', models.CharField(max_length=10, verbose_name='Китайский размер')),
                ('eu', models.CharField(max_length=10, verbose_name='Европейский размер')),
                ('us', models.CharField(max_length=10, verbose_name='Американский размер')),
            ],
            options={
                'verbose_name': 'Размер одежды',
                'verbose_name_plural': 'Размеры одежды',
            },
        ),
        migrations.CreateModel(
            name='RSSSubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telegram_id', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Подписка на RSS',
                'verbose_name_plural': 'Подписки на RSS',
            },
        ),
        migrations.CreateModel(
            name='ClothesInStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_count', models.PositiveIntegerField()),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_in_stock', to='main.clothes')),
                ('clothes_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_in_stock', to='main.clothescolor')),
                ('clothes_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_in_stock', to='main.clothessize')),
            ],
            options={
                'verbose_name': 'Одежда в наличии',
                'verbose_name_plural': 'Одежда в наличии',
            },
        ),
    ]
