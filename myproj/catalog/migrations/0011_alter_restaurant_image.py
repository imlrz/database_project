# Generated by Django 4.1 on 2024-05-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='404.png', upload_to='../media/restaurants/'),
        ),
    ]