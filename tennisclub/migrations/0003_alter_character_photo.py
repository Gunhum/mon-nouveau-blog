# Generated by Django 4.2.7 on 2023-11-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennisclub', '0002_rename_race_character_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='photo',
            field=models.ImageField(upload_to='static/image/'),
        ),
    ]
