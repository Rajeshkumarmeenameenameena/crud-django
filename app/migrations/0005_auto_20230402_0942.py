# Generated by Django 3.0.14 on 2023-04-02 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230402_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='passwoed',
            new_name='password',
        ),
    ]