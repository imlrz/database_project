# Generated by Django 4.1 on 2024-05-28 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_dish_image_alter_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comm_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='catalog.comment'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(choices=[('W', 'West Campus'), ('E', 'East Campus'), ('O', 'Other places'), ('J', 'Jinzhai Road'), ('H', 'Huangshan Road')], default='O', max_length=1),
        ),
    ]