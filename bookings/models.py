from uuid import uuid4
from django.db import models
from users.models import User
from enum import Enum

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40, unique=True, null=False)
    price = models.IntegerField(null=False)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return self.name
    
class BookingStatus(Enum) :
    in_process="IN_PROCESS"
    confirmed="CONFIRMED"
    rejected="REJECTED"
    
class Booking((models.Model)):

    BOOKING_STATUSES = [
        (BookingStatus.in_process.value, 'IN_PROCESS'),
        (BookingStatus.confirmed.value, 'CONFIRMED'),
        (BookingStatus.rejected.value, 'REJECTED')
    ]

    #booing_id, user_id, services[], prices, duration, date, start_time, end_time, status 
    booking_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.CharField(max_length=1000, null=False)
    price = models.IntegerField(null=False)
    duration = models.IntegerField(null=False)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=True)
    status = models.CharField(max_length=30, choices=BOOKING_STATUSES, default="IN_PROCESS")
    
