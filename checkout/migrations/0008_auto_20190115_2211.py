# Generated by Django 2.1.1 on 2019-01-15 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20190115_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='saleproduct',
            name='sale',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='SaleProduct',
        ),
    ]
