# Generated by Django 2.1 on 2018-09-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20180911_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=6),
        ),
    ]