# Generated by Django 4.1 on 2022-08-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_plant_pots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot',
            name='size',
            field=models.CharField(max_length=30),
        ),
    ]
