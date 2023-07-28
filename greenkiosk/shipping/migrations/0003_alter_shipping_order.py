# Generated by Django 4.2.3 on 2023-07-21 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_shopping_carts'),
        ('shipping', '0002_remove_shipping_order_number_shipping_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]
    