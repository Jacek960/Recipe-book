# Generated by Django 2.2.15 on 2020-08-18 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0008_ingredients_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='owner',
        ),
    ]
