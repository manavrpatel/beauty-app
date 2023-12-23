from django.contrib import admin

# Register your models here
from .models.booking import Booking
from .models.service import Service

# Register your models here.
admin.site.register(Service)
admin.site.register(Booking)