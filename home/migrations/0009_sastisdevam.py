# Generated by Django 5.0.1 on 2024-01-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_idare_yonetim'),
    ]

    operations = [
        migrations.CreateModel(
            name='SastisDevam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='media')),
                ('baslik', models.TextField(max_length=200)),
                ('aciklama', models.TextField(max_length=1000)),
            ],
        ),
    ]
