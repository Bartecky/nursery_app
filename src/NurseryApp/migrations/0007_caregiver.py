# Generated by Django 2.1.5 on 2019-01-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NurseryApp', '0006_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
    ]
