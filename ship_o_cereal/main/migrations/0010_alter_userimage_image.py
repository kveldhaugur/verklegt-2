# Generated by Django 3.2 on 2021-05-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='Image',
            field=models.ImageField(upload_to='static/images/userimages'),
        ),
    ]
