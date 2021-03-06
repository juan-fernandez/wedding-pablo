# Generated by Django 2.1.4 on 2018-12-25 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=30, verbose_name='Título')),
                ('slug', models.TextField(max_length=20, verbose_name='URL')),
                ('content', models.TextField(max_length=500, verbose_name='Contenido')),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='attendee',
            options={'verbose_name': 'Asistente', 'verbose_name_plural': 'Asistentes'},
        ),
    ]
