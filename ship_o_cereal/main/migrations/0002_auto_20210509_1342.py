# Generated by Django 3.2 on 2021-05-09 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='AccountID',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ItemsInOrder',
        ),
        migrations.RemoveField(
            model_name='ordercontains',
            name='ItemID',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='AccountConnected',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderContains',
        ),
    ]
