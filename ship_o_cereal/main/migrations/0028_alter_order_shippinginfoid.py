# Generated by Django 3.2 on 2021-05-13 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_ordercontains_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ShippingInfoID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userinfo'),
        ),
    ]
