# Generated by Django 3.2 on 2021-05-12 17:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_items_image_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='DatePurchased',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
