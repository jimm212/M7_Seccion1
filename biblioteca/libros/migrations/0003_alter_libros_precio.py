# Generated by Django 5.1.3 on 2024-11-16 00:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_alter_libros_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(10000.99)]),
        ),
    ]
