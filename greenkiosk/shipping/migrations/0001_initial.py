# Generated by Django 4.2.3 on 2023-07-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=32)),
                ('carrier', models.CharField(max_length=255)),
                ('tracking_number', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=32)),
                ('estimated_delivery', models.DateField()),
            ],
        ),
    ]