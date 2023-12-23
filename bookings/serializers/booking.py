from rest_framework.serializers import ModelSerializer
from bookings.models.booking import Booking
from bookings.models.service import Service

class BookingCreate(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {'booking_id': {'required': False}}