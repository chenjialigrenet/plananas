# Generated by Django 4.0.1 on 2022-03-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_planner', '0002_alter_ingredient_unit_alter_meal_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
    ]
