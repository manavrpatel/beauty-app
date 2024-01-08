from rest_framework.serializers import ModelSerializer
from bookings.models.booking import Booking
from bookings.models.service import Service


class BookingConfirm(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']
