# Generated by Django 2.1.7 on 2019-03-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_match_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
