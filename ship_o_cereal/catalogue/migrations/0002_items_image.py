# Generated by Django 3.2 on 2021-05-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='Image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
