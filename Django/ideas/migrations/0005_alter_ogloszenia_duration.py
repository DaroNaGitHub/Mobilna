# Generated by Django 4.2.11 on 2024-12-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_ogloszenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogloszenia',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]
