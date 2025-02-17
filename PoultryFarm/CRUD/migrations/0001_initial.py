# Generated by Django 5.1.5 on 2025-01-25 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chicken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('health_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Egg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.IntegerField()),
                ('date_collected', models.DateField()),
                ('chicken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.chicken')),
            ],
        ),
    ]
