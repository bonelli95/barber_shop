# Generated by Django 5.0.4 on 2024-05-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_shop', '0006_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/'),
        ),
    ]