# Generated by Django 4.1.1 on 2022-09-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakestore', '0009_remove_cart_total_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_ordering',
            field=models.IntegerField(default=0),
        ),
    ]