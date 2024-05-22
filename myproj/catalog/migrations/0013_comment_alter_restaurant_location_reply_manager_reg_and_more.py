# Generated by Django 4.1 on 2024-05-22 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0012_alter_restaurant_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='COMMENT',
            fields=[
                ('comm_ID', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.FloatField()),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(choices=[('W', 'West Campus'), ('E', 'East Campus'), ('O', 'Other places')], default='O', max_length=1),
        ),
        migrations.CreateModel(
            name='REPLY',
            fields=[
                ('reply_ID', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('comm_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.comment')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MANAGER_REG',
            fields=[
                ('reg_ID', models.AutoField(primary_key=True, serialize=False)),
                ('evidence', models.ImageField(upload_to='evidences/restaurants/')),
                ('resta_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.restaurant')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DISH',
            fields=[
                ('dish_ID', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(max_length=20)),
                ('tag', models.CharField(default='', max_length=4)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(default='404.png', upload_to='dishes/')),
                ('onsale', models.BooleanField(default=True)),
                ('more_Info', models.CharField(blank=True, max_length=200, null=True)),
                ('resta_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='DELETE_RESTA',
            fields=[
                ('delete_ID', models.AutoField(primary_key=True, serialize=False)),
                ('evidence', models.ImageField(upload_to='evidences/delete/')),
                ('resta_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='dish_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.dish'),
        ),
        migrations.AddField(
            model_name='comment',
            name='resta_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.restaurant'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='manager_reg',
            constraint=models.UniqueConstraint(fields=('resta_ID', 'user_ID'), name='his_restaurant'),
        ),
        migrations.AddConstraint(
            model_name='dish',
            constraint=models.UniqueConstraint(fields=('resta_ID', 'dish_name'), name='unique_dish'),
        ),
    ]