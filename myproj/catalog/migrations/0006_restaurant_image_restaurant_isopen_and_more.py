# Generated by Django 4.1 on 2024-05-21 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0005_restaurant_avg_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='isopen',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='AVG_grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(choices=[('WEST', 'West Campus'), ('EAST', 'East Campus'), ('OTHR', 'Other places')], default='OTHR', max_length=4),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='more_Info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='resta_name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='tag',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='time_close',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='time_open',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
