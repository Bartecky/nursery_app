# Generated by Django 2.1.5 on 2019-01-09 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NurseryApp', '0014_auto_20190109_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='registration_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
