# Generated by Django 2.1.4 on 2018-12-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0009_auto_20181229_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(max_length=2000, verbose_name='Contenido'),
        ),
    ]
