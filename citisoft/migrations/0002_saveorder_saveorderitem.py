# Generated by Django 5.0.1 on 2024-03-08 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citisoft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saveOrderId', models.CharField(max_length=100, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='citisoft.client')),
            ],
        ),
        migrations.CreateModel(
            name='SaveOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saveorder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='citisoft.saveorder')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citisoft.vendor')),
            ],
        ),
    ]
