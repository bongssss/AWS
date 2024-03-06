# Generated by Django 5.0.1 on 2024-03-06 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citisoft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved_vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='vendorr',
            name='address',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='vendorr',
            name='contact_tel',
            field=models.CharField(max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='vendorr',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='vendorr',
            name='location',
            field=models.CharField(max_length=1250, null=True),
        ),
        migrations.AlterField(
            model_name='vendorr',
            name='num_of_eployees',
            field=models.IntegerField(null=True),
        ),
    ]
