# Generated by Django 3.1.7 on 2021-03-23 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_doctor_patients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_clinique',
            old_name='medecin',
            new_name='Doctor',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='patients',
        ),
    ]
