# Generated by Django 5.0 on 2024-02-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NikHospital', '0003_alter_booking_age_alter_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='conform_password',
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
