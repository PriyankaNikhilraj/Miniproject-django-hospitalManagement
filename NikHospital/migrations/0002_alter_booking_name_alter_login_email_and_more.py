# Generated by Django 5.0 on 2024-02-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NikHospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='conform_password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phon',
            field=models.CharField(max_length=50),
        ),
    ]
