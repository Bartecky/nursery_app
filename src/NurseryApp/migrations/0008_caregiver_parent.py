# Generated by Django 2.1.5 on 2019-01-08 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NurseryApp', '0007_caregiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregiver',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='NurseryApp.Parent'),
            preserve_default=False,
        ),
    ]
