# Generated by Django 4.1 on 2022-08-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_pot'),
    ]

    operations = [
        migrations.AddField(
            model_name='pot',
            name='color',
            field=models.CharField(default='white', max_length=50),
            preserve_default=False,
        ),
    ]
