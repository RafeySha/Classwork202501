# Generated by Django 5.1.5 on 2025-01-25 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egg',
            old_name='quality',
            new_name='quantity',
        ),
    ]
