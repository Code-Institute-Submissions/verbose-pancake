# Generated by Django 2.1.1 on 2018-12-21 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvote',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
