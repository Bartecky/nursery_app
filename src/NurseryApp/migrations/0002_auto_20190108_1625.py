# Generated by Django 2.1.5 on 2019-01-08 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NurseryApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'ordering': ['last_name'], 'verbose_name_plural': 'children'},
        ),
    ]
