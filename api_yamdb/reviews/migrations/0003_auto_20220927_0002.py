# Generated by Django 2.2.19 on 2022-09-26 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220926_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=200, verbose_name='Текст комментария'),
        ),
    ]
