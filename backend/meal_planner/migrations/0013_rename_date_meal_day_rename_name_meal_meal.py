# Generated by Django 4.0.1 on 2022-03-29 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal_planner', '0012_alter_recipe_photo_alter_user_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='date',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='name',
            new_name='meal',
        ),
    ]