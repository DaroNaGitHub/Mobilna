# Generated by Django 4.2.11 on 2024-12-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
