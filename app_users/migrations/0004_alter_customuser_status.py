# Generated by Django 4.1 on 2022-08-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_alter_customuser_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.TextField(blank=True, default='', max_length=140, verbose_name='status'),
        ),
    ]