# Generated by Django 3.2 on 2021-05-10 16:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('main', '0014_sessionhistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sessionhistory',
        ),
        migrations.CreateModel(
            name='SessionHistory',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID')),
                ('SessionID',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, serialize=False,
                                   to='sessions.session')),
                ('HistoryStr', models.CharField(max_length=255)),
            ],
        ),
    ]