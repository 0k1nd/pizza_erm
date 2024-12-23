# Generated by Django 5.1.3 on 2024-11-25 09:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('canceled', 'canceled')], max_length=150)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pizzaplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pizza_app.pizzaplace')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='pizza_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='pizza_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pizzaplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='pizza_app.pizzaplace')),
            ],
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_product', to='pizza_app.sale')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sale', to='pizza_app.product')),
            ],
        ),
    ]
