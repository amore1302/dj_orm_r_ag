# Generated by Django 2.2.4 on 2020-12-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_owner_own_flat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='fio',
        ),
        migrations.AddField(
            model_name='owner',
            name='owner_deprecated',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
