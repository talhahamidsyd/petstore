# Generated by Django 5.1.1 on 2024-10-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='grant_total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
