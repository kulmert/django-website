# Generated by Django 5.0.1 on 2024-01-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_sastisdevam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeri',
            name='resim',
            field=models.ImageField(upload_to='media'),
        ),
    ]
