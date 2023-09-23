# Generated by Django 3.2.9 on 2022-06-12 05:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0003_auto_20220607_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
