# Generated by Django 2.1 on 2018-09-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20180911_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_create_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_pickup_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_return_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup_store_phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='return_store_phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_phone',
            field=models.CharField(max_length=50),
        ),
    ]
