# Generated by Django 4.1 on 2022-08-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, verbose_name='Date of birth: '),
        ),
    ]
