# Generated by Django 2.1.7 on 2019-03-30 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20190328_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
