# Generated by Django 2.1.4 on 2018-12-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_auto_20181229_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]