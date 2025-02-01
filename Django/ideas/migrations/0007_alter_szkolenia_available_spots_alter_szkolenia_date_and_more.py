# Generated by Django 4.2.11 on 2024-12-27 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0006_rename_ogloszenia_szkolenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='szkolenia',
            name='available_spots',
            field=models.PositiveIntegerField(verbose_name='Wolne miejsca'),
        ),
        migrations.AlterField(
            model_name='szkolenia',
            name='date',
            field=models.DateField(verbose_name='Data szkolenia'),
        ),
        migrations.AlterField(
            model_name='szkolenia',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='Czas trwania (dni)'),
        ),
        migrations.AlterField(
            model_name='szkolenia',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Tytuł szkolenia'),
        ),
        migrations.CreateModel(
            name='Zapis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zapis_date', models.DateTimeField(auto_now_add=True)),
                ('szkolenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.szkolenia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
