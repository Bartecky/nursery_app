# Generated by Django 2.1.5 on 2019-01-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NurseryApp', '0004_auto_20190108_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
