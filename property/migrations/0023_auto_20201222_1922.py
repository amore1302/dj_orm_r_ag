# Generated by Django 2.2.4 on 2020-12-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_auto_20201221_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
    ]