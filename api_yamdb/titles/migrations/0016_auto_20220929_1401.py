# Generated by Django 2.2.16 on 2022-09-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0015_auto_20220926_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
