# Generated by Django 5.0.4 on 2024-05-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_shop', '0003_alter_fotografia_categoria_alter_fotografia_foto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='titulo',
            field=models.CharField(default='', max_length=50),
        ),
    ]
