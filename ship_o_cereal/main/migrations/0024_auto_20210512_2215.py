# Generated by Django 3.2 on 2021-05-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_order_totalprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='TotalPrice',
        ),
        migrations.AddField(
            model_name='order',
            name='TotalPrice',
            field=models.IntegerField(default=0),
        ),
    ]