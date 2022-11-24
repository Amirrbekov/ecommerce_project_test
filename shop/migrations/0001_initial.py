# Generated by Django 4.1.3 on 2022-11-23 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(upload_to='Brand')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(blank=True, max_length=255)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Card',
                'ordering': ('added_at',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(upload_to='Category')),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('descriptions', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='Product')),
                ('product_max_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.IntegerField(default=1)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='CardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.card')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carditem_product', to='shop.product')),
            ],
            options={
                'db_table': 'CardItem',
            },
        ),
    ]