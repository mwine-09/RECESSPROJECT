# Generated by Django 4.1.1 on 2022-09-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakestore', '0005_remove_cart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_ordering',
            field=models.IntegerField(db_column='total_ordering', default=0),
        ),
    ]