# Generated by Django 2.1.7 on 2019-03-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0006_auto_20190330_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
