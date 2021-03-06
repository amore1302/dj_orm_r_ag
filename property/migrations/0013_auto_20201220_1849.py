# Generated by Django 2.2.4 on 2020-12-20 15:49

from django.db import migrations
import phonenumbers

def set_field_new_building_in_floor(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        owner_phone = flat.owners_phonenumber
        phone_number = phonenumbers.parse(owner_phone, "RU")
        if not phonenumbers.is_possible_number(phone_number):
            error_str = "Телефон {0} содержит неправильное колво цифр"
            print(error_str)
            continue
        if not phonenumbers.is_valid_number(phone_number):
            error_str = "Телефон {0} неправильный -не прошел валидациюр"
            print(error_str)
            continue
        flat.owner_pure_phone = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()

def clear_field_new_building_in_floor(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        flat.owner_pure_phone = ''
        flat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20201220_1844'),
    ]

    operations = [
        migrations.RunPython(set_field_new_building_in_floor, clear_field_new_building_in_floor),
    ]
