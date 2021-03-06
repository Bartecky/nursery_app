# Generated by Django 2.1.5 on 2019-01-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NurseryApp', '0010_child_day_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='activity',
            field=models.ManyToManyField(to='NurseryApp.Activity'),
        ),
        migrations.AddField(
            model_name='child',
            name='diet',
            field=models.ManyToManyField(to='NurseryApp.Diet'),
        ),
    ]
