# Generated by Django 4.1 on 2024-05-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='AVG_grade',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
