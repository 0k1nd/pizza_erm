# Generated by Django 5.1.3 on 2024-11-25 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzaplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=1000)),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('snack', 'snack'), ('pizza', 'pizza'), ('dessert', 'dessert'), ('drink', 'drink')], max_length=150)),
                ('unit_of_measurement', models.CharField(choices=[('liters', 'liters'), ('pieces', 'pieces'), ('kilograms', 'kilograms')], max_length=150)),
                ('minimum_stock_level', models.IntegerField(default=50)),
                ('best_before_date', models.FloatField(default=0.1)),
                ('price', models.FloatField(default=0.1)),
                ('supplier', models.ManyToManyField(related_name='products', to='pizza_app.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pizzahouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouses', to='pizza_app.pizzaplace')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_warehouse', to='pizza_app.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_product', to='pizza_app.warehouse')),
            ],
        ),
    ]