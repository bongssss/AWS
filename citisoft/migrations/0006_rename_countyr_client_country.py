# Generated by Django 5.0.1 on 2024-03-14 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citisoft', '0005_client_countyr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='countyr',
            new_name='country',
        ),
    ]
