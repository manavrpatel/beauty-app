# Generated by Django 4.2.8 on 2023-12-20 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]