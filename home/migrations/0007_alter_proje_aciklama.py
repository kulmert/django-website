# Generated by Django 5.0.1 on 2024-01-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_sliders_aciklama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='aciklama',
            field=models.TextField(max_length=1000),
        ),
    ]
