# Generated by Django 3.2 on 2021-05-09 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderContains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('ItemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.items')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ItemsInOrder',
            field=models.ManyToManyField(to='main.OrderContains'),
        ),
    ]
