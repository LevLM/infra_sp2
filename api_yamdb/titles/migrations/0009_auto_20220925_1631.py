# Generated by Django 2.2.16 on 2022-09-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0008_merge_20220925_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]