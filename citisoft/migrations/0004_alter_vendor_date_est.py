# Generated by Django 5.0.1 on 2024-03-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citisoft', '0003_vendor_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='date_est',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]