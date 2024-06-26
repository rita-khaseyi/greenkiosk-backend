# Generated by Django 4.2.3 on 2023-08-20 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_user'),
        ('payment', '0001_initial'),
        ('inventory', '0010_alter_product_image'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
    ]
