# Generated by Django 2.2.4 on 2020-12-18 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_claim'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Claim',
        ),
    ]