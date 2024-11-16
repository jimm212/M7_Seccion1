# Generated by Django 5.1.3 on 2024-11-16 00:13

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(max_length=5)),
            ],
            options={
                'db_table': 'analytics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_p', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2000, 1, 1))])),
            ],
        ),
    ]