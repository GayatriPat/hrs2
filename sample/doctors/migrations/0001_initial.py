# Generated by Django 3.2.9 on 2022-05-22 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('specialities', '0001_initial'),
        ('hospitals', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_name', models.CharField(max_length=255)),
                ('year_of_experience', models.FloatField(max_length=50, null=True)),
                ('doctor_hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospitals.hospital')),
                ('doctor_speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialities.speciality', to_field='speciality_name')),
            ],
        ),
    ]
