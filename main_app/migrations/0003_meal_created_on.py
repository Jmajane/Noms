# Generated by Django 4.0.5 on 2022-06-06 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_meal_alcohol_alter_meal_dairy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
