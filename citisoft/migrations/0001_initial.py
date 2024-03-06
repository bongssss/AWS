# Generated by Django 5.0.1 on 2024-03-05 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendorr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=150, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date_est', models.DateField()),
                ('location', models.CharField(max_length=150, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('contact_tel', models.CharField(max_length=15, null=True)),
                ('num_of_eployees', models.IntegerField(max_length=8, null=True)),
                ('Int_pro_services', models.CharField(max_length=400, null=True)),
                ('business_areas', models.CharField(max_length=400, null=True)),
                ('client_types', models.CharField(max_length=400, null=True)),
                ('cloud_or_native', models.CharField(max_length=100, null=True)),
                ('added_info', models.CharField(max_length=600, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('saved_vendor', models.ManyToManyField(blank=True, null=True, to='citisoft.vendorr')),
            ],
        ),
    ]