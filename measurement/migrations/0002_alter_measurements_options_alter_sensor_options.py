# Generated by Django 4.0.4 on 2022-07-12 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurements',
            options={'verbose_name': 'Показатель', 'verbose_name_plural': 'Показания'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
    ]