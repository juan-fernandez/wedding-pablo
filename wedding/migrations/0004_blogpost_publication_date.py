# Generated by Django 2.1.4 on 2018-12-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0003_auto_20181225_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='publication_date',
            field=models.DateField(null=True, verbose_name='Fecha de publicación automática'),
        ),
    ]
