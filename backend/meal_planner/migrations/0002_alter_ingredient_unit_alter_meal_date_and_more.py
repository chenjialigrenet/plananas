# Generated by Django 4.0.1 on 2022-03-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.PositiveSmallIntegerField(choices=[(1, 'piece'), (2, 'pound'), (3, 'once'), (4, 'miligramme'), (5, 'gramme'), (6, 'kilogramme'), (7, 'mililiter/cc'), (8, 'liter'), (9, 'teaspoon'), (10, 'tablespoon'), (11, 'fluid once'), (12, 'cup'), (13, 'drop'), (14, 'pinch')], default=1),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Breakfast'), (2, 'Lunch'), (3, 'Dinner'), (4, 'Dessert/Snacks')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[(1, '1-Beginner'), (2, '2-Easy'), (3, '3-Normal'), (4, '4-Hard'), (5, '5-Expert')], default=1),
        ),
    ]
