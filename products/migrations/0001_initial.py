# Generated by Django 2.1.2 on 2018-11-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('min_payment', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_amount_paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_area', models.CharField(default='', max_length=254)),
                ('product_need', models.CharField(default='', max_length=254)),
                ('product_complexity', models.CharField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='images')),
                ('product_documents', models.ImageField(upload_to='product_documents')),
            ],
        ),
    ]
