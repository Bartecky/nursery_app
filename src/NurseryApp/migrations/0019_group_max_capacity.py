# Generated by Django 2.1.5 on 2019-01-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NurseryApp', '0018_auto_20190110_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='max_capacity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
