# Generated by Django 4.2.8 on 2023-12-20 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0002_rename_services_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('services', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.CharField(choices=[('IN_PROCESS', 'IN_PROCESS'), ('CONFIRMED', 'CONFIRMED'), ('REJECTED', 'REJECTED')], default='IN_PROCESS', max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
