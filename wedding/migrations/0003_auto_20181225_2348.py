# Generated by Django 2.1.4 on 2018-12-25 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_auto_20181225_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=20, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Título'),
        ),
    ]
